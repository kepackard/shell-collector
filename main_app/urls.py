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
    path('flairs/', views.FlairList.as_view(), name='flair_index'),
    path('flairs/<int:pk>/', views.FlairDetail.as_view(), name='flair_detail'),
    path('flairs/create/', views.FlairCreate.as_view(), name='flair_create'),
    path('flairs/<int:pk>/update/', views.FlairUpdate.as_view(), name='flair_update'),
    path('flairs/<int:pk>/delete/', views.FlairDelete.as_view(), name='flair_delete'),
    path('shells/<int:shell_id>/assoc_flair/<int:flair_id>/',
         views.assoc_flair, name='assoc_flair'),
    path('shells/<int:shell_id>/unassoc_flair/<int:flair_id>/', views.unassoc_flair, name='unassoc_flair'),
]