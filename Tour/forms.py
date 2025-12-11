from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .Views.models import Register,Question
class AdminLogin(AuthenticationForm):
    class Meta:
        model=User
        fields=['username','password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=["username","email","password",]
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model=Register
        fields=["email","password",]
        widgets={
            'password': forms.PasswordInput(),
        }
