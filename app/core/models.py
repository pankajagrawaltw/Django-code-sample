from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TypeAnswer(TimeStampedModel):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Question(TimeStampedModel):
    question = models.CharField(max_length=255)
    answer_type = models.ForeignKey(TypeAnswer, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.question


class Client(TimeStampedModel):
    company_name = models.CharField(max_length=255)
    color = models.CharField(max_length=255, default="#26a69a")
    survey_questions = models.ManyToManyField(Question)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name


class Member(TimeStampedModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class TypeSurveyStatus(TimeStampedModel):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.code


class Survey(TimeStampedModel):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.ForeignKey(TypeSurveyStatus, on_delete=models.CASCADE)
    url_long = models.CharField(max_length=255)
    url_short = models.CharField(max_length=255)
    url_requested_datetime = models.DateTimeField(null=True, blank=True)
    url_generated_datetime = models.DateTimeField(null=True, blank=True)
    url_opened_datetime = models.DateTimeField(null=True, blank=True)
    survey_submitted_datetime = models.DateTimeField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "%s - %s" % (self.member, self.status)


class SurveyResult(TimeStampedModel):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)

    def get_member(self):
        return self.survey.member_id

    def get_survey_submitted_datetime(self):
        return self.survey.survey_submitted_datetime

    def get_question(self):
        return self.question.question

    def get_answer(self):
        return self.answer

    def get_client(self):
        return self.survey.client.id

    def __str__(self):
        return "%s - %s" % (self.survey, self.question)
