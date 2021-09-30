from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
class AddNews(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.ImageField()
    text = forms.CharField(max_length=10000)
    tag = forms.CharField(max_length=50)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=200)

class PostNews(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class RegistartionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']