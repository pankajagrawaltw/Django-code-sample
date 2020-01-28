from django import forms
from app.core.models import Client, Member


class SearchForm(forms.Form):
    start_date = forms.CharField(label='Start Date', max_length=100, required=False)
    end_date = forms.CharField(label='End Date', max_length=100, required=False)
    client_id = forms.ModelChoiceField(queryset=Client.objects.all(), required=False)
    member_id = forms.ModelChoiceField(queryset=Member.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs['class'] = 'datepicker'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'
        self.fields['start_date'].widget.attrs['id'] = 'start_date'
        self.fields['end_date'].widget.attrs['id'] = 'end_date'
        self.fields['member_id'].widget.attrs['id'] = 'member_id'
        self.fields['client_id'].widget.attrs['id'] = 'client_id'