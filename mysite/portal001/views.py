from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from django.utils.safestring import mark_safe
from . import views

# Create your views here.


def curo(request):
    """ A view to return the intro page """
    thispage = 'curo'
    context = {
        'thispage': thispage,
        'arrows': 'noarrows',
        'nexthidden': 'false',
    }

    return render(request, 'curo/intro.html', context)