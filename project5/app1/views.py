from django.shortcuts import render
from django.http import HttpResponse

def first_app1(request):
    return HttpResponse('This is first app  function in django')

def second_app1(request):
    return HttpResponse('This is second function in app1')

def third_app1(request):
    return HttpResponse('this is third function in app1')

def vyshu_app1(request):
    return HttpResponse('my name is vyshu')    
