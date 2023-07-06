from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from .models import Orders
from .forms import OrderForm
from django.db.models import Q


def curo(request):
    """ A view to return the intro page """
    thisOrder = 1234567
    queries = (Q(orderNumber__icontains=thisOrder) |
               Q(orderDescription__icontains=thisOrder))
    orders = Orders.objects.all()
    order_list = (orders.filter(queries)
                  .order_by('orderNumber').first())
    order_list_length = orders.filter(queries).count()
    form = OrderForm(instance=order_list)

    context = {
        'form': form,
        'order_list': order_list,
        'order_list_length': order_list_length,
    }

    return render(request, 'curo/portal.html', context)


def updateOrderForm(request):
    """ Update the order form """
    orderNumber = 12345676
    thisorder = Orders.objects.get(orderNumber=orderNumber)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=thisorder)
        if form.is_valid():
            form.save()
    else:
        return render(request, 'home/home.html')

    context = {
        'form': form,
    }

    return render(request, 'curo/portal.html', context)