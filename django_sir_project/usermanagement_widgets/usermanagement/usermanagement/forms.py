from django import forms

class UserLogin(forms.Form):
      email=forms.EmailField(widget=forms.TextInput(attrs={'class':"form-control border-0"}))
      password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control border-0",'height': 55}))
      