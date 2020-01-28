from django.contrib import admin

from .models import TypeAnswer, Question, Client, Member, TypeSurveyStatus, Survey, SurveyResult


admin.site.register(TypeAnswer)
admin.site.register(Question)
admin.site.register(Client)
admin.site.register(Member)
admin.site.register(TypeSurveyStatus)
admin.site.register(Survey)
admin.site.register(SurveyResult)
