from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    email = forms.CharField(max_length=100,required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput,required=True)


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput,required=True)