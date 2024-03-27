from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile



class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=25, required=True, widget=forms.TextInput())
    email = forms.CharField(max_length=50, required=True, widget=forms.TextInput())
    password1 = forms.CharField(max_length=25, required=True, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=25, required=True, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password1"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=forms.FileInput())
    birthday = forms.DateField(widget=forms.DateInput)
    country = forms.CharField(max_length=10, required=True, widget=forms.TextInput())
    email = forms.EmailField(max_length=50, required=True, widget=forms.EmailInput())

    class Meta:
        model = Profile
        fields = ['avatar', 'birthday', 'country', 'email']