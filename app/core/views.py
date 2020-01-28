import datetime

from django.views import View
from django.utils import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic import TemplateView

from survey.utils import goo_shorten_url
from app.core.models import Member, TypeSurveyStatus, Client, Survey, \
                SurveyResult


class SurveyLink(APIView):

    def get(self, request, client_id, member_id, purchase_order_no):
        response = {"status": False, "message": "Failed", "errors": []}
        url_requested_datetime = datetime.datetime.now()
        url_long = "http://website-url/survey/%s/%s/%s/" % (client_id, member_id, purchase_order_no)
        url_short = url_long  # TODO: Need to call goo_shorten_url(url_long)
        try:
            client = Client.objects.get(id=client_id)
        except Exception as err:
            response["errors"].append({"field": "client_id", "error": "Client does not exist!"})

        try:
            member = Member.objects.get(id=member_id)
        except Exception as err:
            response["errors"].append({"field": "member_id", "error": "Member does not exist!"})

        if len(response["errors"]) > 0:
            return Response(response)

        survey, created = Survey.objects.get_or_create(
            client_id=client_id,
            member_id=member_id,
            status=TypeSurveyStatus.objects.get(code="SURVEY_LINK_GENERATED_AND_SENT")
        )
        survey.status = TypeSurveyStatus.objects.get(code="SURVEY_LINK_GENERATED_AND_SENT")
        survey.url_long = url_long
        survey.url_short = url_short
        survey.url_requested_datetime = url_requested_datetime
        survey.url_generated_datetime = datetime.datetime.now()
        survey.save()

        response["status"] = True
        response["message"] = "Success"
        response["data"] = {"url_short": url_short}
        return Response(response)


class SurveyPage(TemplateView):
    template_name = 'core/survey_questions.html'

    def get_context_data(self, **kwargs):
        context = super(SurveyPage, self).get_context_data(**kwargs)
        client_id = kwargs["client_id"]
        member_id = kwargs["member_id"]
        client = Client.objects.get(id=client_id)
        survey = Survey.objects.get(member_id=member_id)
        context["color"] = survey.client.color
        context["status"] = False
        if survey.status == TypeSurveyStatus.objects.get(code="SURVEY_COMPLETE"):
            context["status"] = True
        else:
            context["survey_questions"] = client.survey_questions.all()
            survey.status = TypeSurveyStatus.objects.get(code="SURVEY_LINK_OPENED_BY_CUSTOMER")
            survey.url_opened_datetime = timezone.now()
            survey.client_id = client_id
            survey.save()
        return context


class SaveSurvey(View):
    def post(self, request, client_id, member_id):
        survey = Survey.objects.get(member_id=member_id, client_id=client_id)
        response = {}
        response["color"] = survey.client.color
        for key, data in request.POST.items():
            if "-" in key:
                survey_result = SurveyResult()
                survey_result.question_id = int(key.split("-")[0])
                survey_result.answer = data
                survey_result.member_id = survey.member_id
                survey.status = TypeSurveyStatus.objects.get(code="SURVEY_COMPLETE")
                survey.survey_submitted_datetime = datetime.datetime.now()
                survey.save()
                survey_result.survey = survey
                survey_result.save()

        return render(
            request, 'core/survey_questions_completed.html', response)
