from django.urls import path

from app.core.views import SurveyLink, SurveyPage, SaveSurvey


urlpatterns = [
    path('survey-link/<int:client_id>/<int:member_id>/<int:purchase_order_no>', SurveyLink.as_view(), name='survey_link'),
    path('survey/<int:client_id>/<int:member_id>/<int:purchase_order_no>', SurveyPage.as_view(), name='survey'),
    path('save_survey/<int:client_id>/<int:member_id>/', SaveSurvey.as_view(), name='save_survey'),
]
