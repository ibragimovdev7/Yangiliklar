from django import forms

class AddNews(forms.Form):
    title = forms.CharField(max_length=200)
    image = forms.ImageField()
    text = forms.CharField(max_length=10000)
    tag = forms.CharField(max_length=50)