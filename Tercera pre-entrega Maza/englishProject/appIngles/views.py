
from django.shortcuts import render

def index(request):
    return render(request,'appIngles/index.html')

def courses(request):
    return render(request,'appIngles/courses.html')

def in_companyTraining(request):
    return render(request,'appIngles/in_companyTraining.html')

def team(request):
    return render(request,'appIngles/team.html')



