from django import forms
from django.forms import ModelForm
from .models import *

class UploadForm(ModelForm):
    class Meta:
        model = File
        fields = ['file']