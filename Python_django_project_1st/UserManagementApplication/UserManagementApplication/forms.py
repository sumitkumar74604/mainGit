from django import forms

class UserLogin(forms.Form):
    email=forms.EmailField()
    password=forms.CharField()