from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name = 'index'),
    path('add_news/',add_news,name='add_news'),
]