from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first_app2(request):
    return HttpResponse('this is fst function in app2')
