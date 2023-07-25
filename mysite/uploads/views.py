from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import UploadFile
import uuid


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
            instance = UploadFile(file_field=request.FILES["file"])
            instance.save()
            messages.success(request, 'Maybe it saved...?')
        else:
            messages.success(request, 'No, it didn`t!')
    else:
        messages.success(request, 'It`s not POST!')
        form = UploadFileForm()
    return render(request, "uploads/upload.html", {"form": form})
