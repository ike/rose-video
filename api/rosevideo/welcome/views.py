from django.shortcuts import render
from django.urls import path
from . import views

def welcome(request):
    return render(request, 'welcome.html')

def forums(request):
    return render(request, 'forums.html')

def roadmap(request):
    return render(request, 'roadmap.html')

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('forums', views.forums, name='forums'),
    path('roadmap', views.roadmap, name='roadmap'),
]

