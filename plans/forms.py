from django import forms
from .models import *
from django.contrib.admin import widgets
from ckeditor.widgets import CKEditorWidget

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ('title', 'price', 'description', 'duration', 'is_dummy')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'ex: Basic, Premium, Standard ...', 'class': 'w3-input w3-border w3-round'}),
            'price': forms.NumberInput(attrs={'placeholder': 'enter price for the plan', 'class': 'w3-input w3-border w3-round'}),
            'description': forms.Textarea(attrs={'placeholder': 'overview', 'class': 'w3-input w3-border w3-round'}),
            'duration': forms.Select(attrs={'placeholder': 'duration of plan', 'class': 'w3-input w3-border w3-round'}),
            'is_dummy': forms.CheckboxInput(attrs={'placeholder': 'is dummy ?', 'class': 'w3-margin w3-check'}),
        }

class SubscribeForm(forms.Form):
    username = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'enter username for any 1 student ', 'class': 'w3-input w3-border w3-round'}),
        initial='username'
        )
    institution = forms.CharField(
        max_length=300, 
        widget=forms.TextInput(attrs={'placeholder': 'enter institution name correctly to filter students', 'class': 'w3-input w3-border w3-round'}),
        initial='institution'
        )

class UpdateUserPlanForm(forms.Form):
    title = forms.CharField(
        max_length=100, 
        widget=forms.TextInput(attrs={'placeholder': 'enter new title', 'class': 'w3-input w3-border w3-round'}),
        )
    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'placeholder': 'enter new price', 'class': 'w3-input w3-border w3-round'})
        )

        