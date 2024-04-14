from django import forms

from career.models import Career
from .models import Stage

class CandidateForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=150)
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    stage = forms.ModelChoiceField(queryset=Stage.objects.all())
    career = forms.ModelChoiceField(queryset=Career.objects.all())

class LoadCSVForm(forms.Form):
    file = forms.FileField()
    stage = forms.ModelChoiceField(queryset=Stage.objects.all())