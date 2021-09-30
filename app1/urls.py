from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name = 'index'),
    path('<int:id>',new_by_id,name='new_by_id'),
    path('add_news/',add_news,name='add_news'),
    path('siyosat/',siyosat,name='siyosat'),
    path('registration/',registrationView,name='registration'),
    path('login/',log_in,name='login'),
    path('logout',log_out,name='logout'),

]