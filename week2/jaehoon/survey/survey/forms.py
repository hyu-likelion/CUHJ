from django import forms

class SurveyForm(forms.Form):
    ans = forms.CharField(widget=forms.Textarea)
    