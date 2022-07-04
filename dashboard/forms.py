from dataclasses import fields
from django import forms
from .models import customer
class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = [ 'utility_name' ,'utility_short_name' ,'utility_state' ,'utility_district' ,'utility_country' ,'utility_postalcode' ,'utility_address' ,'contact_person' ,'contact_email' ,'contact_phnum' ,'contact_mobile' ,'contact_designation' ,'contact_landline' ,'emergency_person' ,'emergency_altperson' ,'emergency_mobile' ,'emergency_altmobile' ,'emergency_officeaddress' ,'emergency_altofficeaddress']