import datetime

from django.urls import reverse
from django.test import TestCase
from django.core.urlresolvers import reverse

from app.core.models import ( TypeAnswer, Question, Member, TypeSurveyStatus, Client, Survey,
                SurveyResult )


class CoreViewsBaseTestCase(TestCase):

    def test_create_type_answers(self):
        self.assertEqual(TypeAnswer.objects.count(), 0)
        self.type_answer_yes_no = TypeAnswer(
            code = "YES_NO",
            description = "Yes No"
        )
        self.type_answer_yes_no.save()
        self.type_answer_freeform = TypeAnswer(
            code = "FREEFORM",
            description = "Freeform Text Field"
        )
        self.type_answer_freeform.save()
        self.type_answer_stars = TypeAnswer(
            code = "STARS",
            description = "Stars"
        )
        self.type_answer_stars.save()
        self.assertEqual(TypeAnswer.objects.count(), 3)

    def test_create_type_survey_status(self):
        self.assertEqual(TypeSurveyStatus.objects.count(), 0)

        self.type_survey_status_request = TypeSurveyStatus(
            code = "SURVEY_LINK_REQUESTED",
            description = "Survey Link Requested"
        )
        self.type_survey_status_request.save()

        self.assertEqual(TypeSurveyStatus.objects.count(), 1)

        self.type_survey_status_sent = TypeSurveyStatus(
            code = "SURVEY_LINK_GENERATED_AND_SENT",
            description = "Survey Link Generated and Sent"
        )
        self.type_survey_status_sent.save()
        self.type_survey_status_opened = TypeSurveyStatus(
            code = "SURVEY_LINK_OPENED_BY_CUSTOMER",
            description = "Survey Link Opened by Customer"
        )
        self.type_survey_status_opened.save()
        self.type_survey_status_complete = TypeSurveyStatus(
            code = "SURVEY_COMPLETE",
            description = "Survey Complete"
        )
        self.type_survey_status_complete.save()
        self.assertEqual(TypeSurveyStatus.objects.count(), 4)

    def test_create_survey(self):
        self.member = Member(
            first_name = "first_name",
            last_name = "last_name"
        )
        self.member.save()
        self.assertEqual(self.member.id, 1)