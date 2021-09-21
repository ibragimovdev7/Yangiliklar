from django.shortcuts import render
from django.http import HttpResponse
from .models import News
from .forms import AddNews
def index(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request,'index.html',context)

def add_news(request):
    form = AddNews()
    if request.method=='POST':
        form = AddNews(request.POST)
        if form.is_valid():
            title = request.POST.get('title')
            text = request.POST['text']
            tag = request.POST.get('tag')
            image = request.FILES['image']
            new = News(title= title, image = image, text = text, tag = tag)
            new.save()
            print("is valid...")
    context = {
        'form':form
    }
    return render(request,'add_news.html',context)