from django.shortcuts import render, redirect
from .models import Shell
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CleaningForm

from django.http import HttpResponse

def home(request):
    return render(request, 'home.html') 

def about(request):
    return render(request, 'about.html')

# def shells_index(request):
#     return render(request, 'shells/index.html', { 'shells': shells })

def shells_index(request):
    shells = Shell.objects.all()
    return render(request, 'shells/index.html', { 'shells': shells })

def shells_detail(request, shell_id):
    shell = Shell.objects.get(id=shell_id)
    cleaning_form = CleaningForm()
    return render(request, 'shells/detail.html', { 
        'shell': shell, 'cleaning_form': cleaning_form
    })

def add_cleaning(request, shell_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.shell_id = shell_id
        new_cleaning.save()
    return redirect('detail', shell_id=shell_id)

class ShellCreate(CreateView):
    model = Shell
    fields = '__all__'

class ShellUpdate(UpdateView):
    model = Shell
    fields = '__all__'

class ShellDelete(DeleteView):
    model = Shell
    success_url = '/shells/'