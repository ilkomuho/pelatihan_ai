from django import forms
from .models import UploadedPhoto

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedPhoto
        fields = ['photo']
