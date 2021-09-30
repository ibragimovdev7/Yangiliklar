from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth import login,logout,authenticate

def index(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request,'index.html',context)

def add_news(request):
    form = AddNews()
    if request.method=='POST':
        form = AddNews(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            text = request.POST['text']
            tag = request.POST.get('tag')
            image = request.FILES['image']
            new = News(title= title, image = image, text = text, tag = tag)
            new.save()

    context = {
        'form':form
    }
    return render(request,'add_news.html',context)

def siyosat(request):
    print(News.objects.all())
    news = News.objects.filter(tag__iexact = 'siyOsat')
    context = {
        'news':news
    }
    return render(request,'index.html',context)

def new_by_id(request, id):
    new = News.objects.get(id = id)
    context = {
        'new':new
    }
    return render(request,'new_by_id.html',context)



def registrationView(request):
    form = RegistartionForm(request.POST)
    if form.is_valid():
        form.save()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('index')
    context = {
        'form':form
    }
    return render(request,'registration.html',context)

def log_in(request):
    form = LoginForm()

    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request=request,username=username,password=password)
    if user:
        login(request,user)
        return redirect('index')
    context = {
        'form':form
    }
    return render(request,'login.html',context)


def log_out(request):
    user = request.user
    if user:
        logout(request)
    return redirect('login')
