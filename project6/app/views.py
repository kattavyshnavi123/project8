from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_app(request):
    return HttpResponse('everything happens for a reason')