from django import forms

class UserLogin(forms.Form):
      email=forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':"form-control border-0",'placeholder':'Email'}))
      password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':"form-control border-0",'placeholder':'Password'}))
      
class UserRegistration(forms.Form):
      name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control border-0",'placeholder':'Name'}))

      email=forms.EmailField(label='',widget=forms.EmailInput(attrs={'class':"form-control border-0",'placeholder':'Email'}))
      
      password=forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':"form-control border-0",'placeholder':'Password'}))

      mobile=forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control border-0",'placeholder':'Mobile'}))

      gender=forms.CharField(label='',widget=forms.TextInput(attrs={'class':"form-control border-0",'placeholder':'Gender'}))

      address=forms.CharField(label='',widget=forms.Textarea(attrs={'class':"form-control border-0",'placeholder':'Address'}))

      dob=forms.DateField(label='',widget=forms.DateInput(attrs={'class':"form-control border-0",'type':'date'}))
      
