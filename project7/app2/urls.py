from app2.views import *
from django.urls import path
app_name='app2'
urlpatterns=[
    path('app2/',first_app2,name='first_app2')
]
