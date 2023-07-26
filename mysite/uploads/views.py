from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from portal001.models import Orders, Contractors, Notifications
from portal001.forms import OrderForm
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import UploadFile
import uuid


def uploadFile(request, orderno):
    """ A view to return the upload page """

    form = UploadFileForm()
    uploadlist = UploadFile.objects.all().order_by('-orderNumber')

    context = {
        'form': form,
        'orderno': orderno,
        'uploadlist': uploadlist,
    }

    return render(request, 'uploads/upload.html', context)


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'File has been saved.')
        else:
            messages.success(request, 'File didn`t save!')
    else:
        messages.success(request, 'Oops! Something went wrong.')
        form = UploadFileForm()

    orderno = form.data['orderNumber']
    orders = Orders.objects.all()
    this_order = Orders.objects.get(orderNumber=orderno)
    order_list_length = orders.filter(orderNumber=orderno).count()
    form = OrderForm(instance=this_order)
    contractors = Contractors.objects.all()
    page = 'orderdetail'

    context = {
        'orderno': orderno,
        'form': form,
        'order_list_length': order_list_length,
        'contractors': contractors,
        'page': page,
    }

    return render(request, 'curo/orderdetail.html', context)
