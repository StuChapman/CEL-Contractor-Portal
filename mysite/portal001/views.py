from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from .models import Orders
from .forms import OrderForm
from django.db.models import Q
from django.utils import timezone


def curo(request):
    """ A view to return the intro page """

    orderlist = Orders.objects.all().order_by('-orderNumber')
    order_list_length = orderlist.count()

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
    }

    return render(request, 'curo/orderlist.html', context)


def selectOrder(request, orderno):
    """ Update the order form """

    orders = Orders.objects.all()
    this_order = Orders.objects.get(orderNumber=orderno)
    order_list_length = orders.filter(orderNumber=orderno).count()
    form = OrderForm(instance=this_order)

    context = {
        'orderno': orderno,
        'form': form,
        'order_list_length': order_list_length,
    }

    return render(request, 'curo/orderdetail.html', context)


def updateOrder(request):
    """ Update the order form """

    if request.GET:
        if 'order_number' in request.GET:
            orderno = request.GET['order_number']
            thisorder = Orders.objects.get(orderNumber=orderno)
    else:
        messages.success(request, 'Oops! Something went wrong.')
        orderlist = Orders.objects.all().order_by('-orderNumber')
        order_list_length = orderlist.count()

        context = {
            'orderlist': orderlist,
            'order_list_length': order_list_length,
        }

        return render(request, 'curo/orderlist.html', context)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=thisorder)
        if form.is_valid():
            form.save()
    else:
        messages.success(request, 'Oops! Something went wrong.')
        orderlist = Orders.objects.all().order_by('-orderNumber')
        order_list_length = orderlist.count()

        context = {
            'orderlist': orderlist,
            'order_list_length': order_list_length,
        }

        return render(request, 'curo/orderlist.html', context)

    context = {
        'orderno': orderno,
        'form': form,
        'order_list_length': '1',
    }

    return render(request, 'curo/orderdetail.html', context)


def createOrder(request):
    """ Update the order form """

    orders = Orders.objects.all()

    if request.method == 'POST':
        print(request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        return render(request, 'home/home.html')

    context = {
        'form': form,
    }

    return render(request, 'curo/portal.html', context)


def searchOrders(request):
    """ A view to return a list of orders that meet the search criteria """

    orderlist = Orders.objects.all().order_by('-orderNumber')
    order_list_length = orderlist.count()

    if request.GET:
        if 'search_string' in request.GET:
            searchstring = request.GET['search_string']
            queries = (Q(orderNumber__icontains=searchstring) |
                       Q(orderDescription__icontains=searchstring) |
                       Q(name__icontains=searchstring) |
                       Q(address__icontains=searchstring) |
                       Q(contractor__icontains=searchstring) |
                       Q(primaryContact__icontains=searchstring) |
                       Q(secondaryContact__icontains=searchstring) |
                       Q(notes__icontains=searchstring))
            orders = Orders.objects.all()
            orderlist = (orders.filter(queries)
                         .order_by('orderNumber'))
            order_list_length = orders.filter(queries).count()
    else:
        messages.success(request, 'Oops! Something went wrong.')

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
    }

    return render(request, 'curo/orderlist.html', context)
