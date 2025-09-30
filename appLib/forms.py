from django import forms
from .models import FileLibrary

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileLibrary
        fields = ['title', 'description', 'file']

