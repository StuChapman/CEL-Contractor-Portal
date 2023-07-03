from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from django.utils.safestring import mark_safe
from . import views
from .models import Orders
from .forms import OrderForm

# Create your views here.


def curo(request):
    """ A view to return the intro page """
    orders = Orders.objects.all()
    thisOrder = '12345678'
    order_result = (orders.filter
                    (orderNumber=thisOrder))
    thisOrder = '12345678'
    order_form = OrderForm(initial={
        'orderNumber': order_result.orderNumber,
        'orderDescription': order_result.orderDescription,
        'name': order_result.name,
        'address': order_result.address,
        'contractor': order_result.contractor,
        'appointmentDate': order_result.appointmentDate,
        'primaryContact': order_result.primaryContact,
        'secondaryContact': order_result.secondaryContact,
        'notes': order_result.notes,
        'dateLastUpdate': order_result.dateLastUpdate,
    })
    context = {
        'order_form': order_form,
    }

    return render(request, 'curo/portal.html', context)