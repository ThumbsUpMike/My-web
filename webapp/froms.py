from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    contact = forms.CharField()
    body = forms.CharField()
