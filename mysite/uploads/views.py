from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from django.http import HttpResponseRedirect
from .forms import UploadFileForm


def uploadFile(request, orderno):
    """ A view to return the upload page """

    form = UploadFileForm()

    context = {
        'form': form,
        'orderno': orderno,
    }

    return render(request, 'uploads/upload.html', context)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            messages.success(request, 'File saved.')
    else:
        messages.success(request, 'Oops! Something went wrong.')
    
    context = {
        'form': form,
    }

    return render(request, 'uploads/upload.html', context)


def handle_uploaded_file(f):
    with open("uploadedfiles/name.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
