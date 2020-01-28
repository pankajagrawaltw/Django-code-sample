from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SearchForm
from app.core.models import SurveyResult


class Dashboard(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/")
        return render(
            request, 'admin/dashboard.html',
            {"search_form": SearchForm})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("/")
        response = {}
        response["search_form"] = SearchForm(request.POST)
        client_id = request.POST.get('client_id')
        member_id = request.POST.get('member_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        survey_result = SurveyResult.objects.all()
        if member_id:
            survey_result = survey_result.filter(survey__member_id=member_id)
        if client_id:
            survey_result = survey_result.filter(survey__client_id=client_id)
        if start_date and end_date:
            survey_result = survey_result.filter(created_at__date__range=[start_date, end_date])
        response["result"] = survey_result
        return render(request, 'admin/dashboard.html', response)
