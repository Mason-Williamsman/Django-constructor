from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django.forms import fields

class AppCreationForm(forms.Form):
     application_name = forms.CharField()


class ProjectCreationForm(forms.Form):
     project_name = forms.CharField()
     project_path = forms.CharField()
     project_public_url = forms.CharField()

     # def save(self):
     #      pass