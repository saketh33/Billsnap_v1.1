from .models import *
from django import forms
from .models import *
from django.contrib.admin import widgets
from ckeditor.widgets import CKEditorWidget
from accounts.models import *

class AppForm(forms.ModelForm):
    class Meta:
        model = applists
        fields = ('appimg', 'author')
        widgets = {
            'appimg': forms.FileInput(attrs={'placeholder': '', 'class': 'w3-input w3-border w3-round'}),
            'author': forms.Select(attrs={'placeholder': 'duration of plan', 'class': 'w3-input w3-border w3-round'})
        }



