from django.shortcuts import render
from django.views import generic
from django.contrib.auth import views
from .models import User

class ProfileView(generic.DetailView):
    template_name = "users/profile.html"
    model = User

class LogoutView(views.LogoutView):
    success_url = reverse('cammon:home')
    
