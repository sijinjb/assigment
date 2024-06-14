from django import forms

class loginform(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)

class registrationform(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

