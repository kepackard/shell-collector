from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shells/', views.shells_index, name='index'),
    path('shells/<int:shell_id>/', views.shells_detail, name='detail'),
    path('shells/create/', views.ShellCreate.as_view(), name='shells_create'),
    path('shells/<int:pk>/update/', views.ShellUpdate.as_view(), name='shells_update'),
    path('shells/<int:pk>/delete/', views.ShellDelete.as_view(), name='shells_delete'),
    path('shells/<int:shell_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
]