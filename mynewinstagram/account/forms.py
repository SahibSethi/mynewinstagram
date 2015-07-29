from django import forms
from .models import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields='__all__'

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False) 

