from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shells/', views.shells_index, name='index'),
    path('shells/<int:shell_id>/', views.shells_detail, name='detail'),
]