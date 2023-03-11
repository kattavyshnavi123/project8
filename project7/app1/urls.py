from app1.views import *
from django.urls import path
app_name='app1'
urlpatterns=[
    path('app1/',first_app1,name='first_app1')
]