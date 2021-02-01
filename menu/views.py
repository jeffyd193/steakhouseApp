from django.shortcuts import render
from .models import Food
from django.views.generic import ListView
# Create your views here.

class Menu(ListView):
    model = Food