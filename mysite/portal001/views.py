from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from .models import Orders
from .forms import OrderForm
from django.db.models import Q


# Create your views here.


def curo(request):
    """ A view to return the intro page """

    return render(request, 'curo/home.html')


def indexes(request):
    """ A view to return the index page """

    return render(request, 'home/home.html')
