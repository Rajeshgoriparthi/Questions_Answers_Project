from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput}

class QuestionsForm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=['questions']


class AnswersForm(forms.ModelForm):
    class Meta:
        model=Answers
        fields=['questions','answerd_by']