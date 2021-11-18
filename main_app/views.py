from django.shortcuts import render
from .models import Shell

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

def shells_index(request):
    return render(request, 'shells/index.html', { 'shells': shells })

def shells_index(request):
    shells = Shell.objects.all()
    return render(request, 'shells/index.html', { 'shells': shells })

def shells_detail(request, shell_id):
    shell = Shell.objects.get(id=shell_id)
    return render(request, 'shells/detail.html', { 'shell': shell })