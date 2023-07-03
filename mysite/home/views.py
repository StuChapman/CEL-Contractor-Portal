from django.shortcuts import render
from django.urls import path
from . import views

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')
