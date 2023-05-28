from django.shortcuts import render
from app.models import *

# Create your views here.
def display_dept(request):
    LOD=DEPT.objects.all()
    d={'dept':LOD}
    return render(request,'dept.html',d)

def display_emp(request):
    LOC=EMP.objects.all()
    d={'emp':LOE}
    return render(request,'emp.html',d)    

