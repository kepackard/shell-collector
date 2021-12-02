from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from .models import Shell, Flair
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CleaningForm
from django.views.generic import ListView

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
    cleaning_form = CleaningForm()
    
    flairs_shell_doesnt_have = Flair.objects.exclude(
        id__in=shell.flairs.all().values_list('id'))

    return render(
        request, 
        'shells/detail.html', { 
            'shell': shell,     
            'cleaning_form': cleaning_form, 
            'flairs': flairs_shell_doesnt_have
    })

def add_cleaning(request, shell_id):
    form = CleaningForm(request.POST)
    print(form._errors)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.shell_id = shell_id
        new_cleaning.save()
    return redirect('detail', shell_id=shell_id)

def assoc_flair(request, shell_id, flair_id):
    Shell.objects.get(id=shell_id).flairs.add(flair_id)
    return redirect('detail', shell_id=shell_id)

def unassoc_flair(request, shell_id, flair_id):
    Shell.objects.get(id=shell_id).flairs.remove(flair_id)
    return redirect('detail', pk=shell_id)

class ShellIndex(ListView):
    model = Shell
    template_name = 'shells/index.html'

    def get_queryset(self):
        queryset = Shell.objects.filter(user=self.request.user)
        return queryset
class ShellCreate(CreateView):
    model = Shell
    fields = '__all__'

class ShellUpdate(UpdateView):
    model = Shell
    fields = '__all__'

class ShellDelete(DeleteView):
    model = Shell
    success_url = '/shells/'

class FlairCreate(CreateView):
    model = Flair
    fields = ('name', 'color')


class FlairUpdate(UpdateView):
    model = Flair
    fields = ('name', 'color')


class FlairDelete(DeleteView):
    model = Flair
    success_url = '/flairs/'


class FlairDetail(DetailView):
    model = Flair
    template_name = 'flairs/detail.html'


class FlairList(ListView):
    model = Flair
    template_name = 'flairs/index.html'