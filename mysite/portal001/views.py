from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from .models import Orders, Contractors, Notifications
from uploads.models import UploadFile
from .forms import OrderForm
from django.db.models import Q
from django.utils import timezone
from django.utils.safestring import mark_safe
import re


def curo(request):
    """ A view to return the intro page """

    orderlist = Orders.objects.all().order_by('-orderNumber')
    order_list_length = orderlist.count()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    page = 'orderlist'

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
        'page': page,
        'uploadlist': uploadlist,
    }

    return render(request, 'curo/orderlist.html', context)


def selectOrder(request, orderno):
    """ Update the order form """

    orders = Orders.objects.all()
    this_order = Orders.objects.get(orderNumber=orderno)
    order_list_length = orders.filter(orderNumber=orderno).count()
    form = OrderForm(instance=this_order)
    contractors = Contractors.objects.all()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    page = 'orderdetail'

    context = {
        'orderno': orderno,
        'form': form,
        'order_list_length': order_list_length,
        'contractors': contractors,
        'page': page,
        'uploadlist': uploadlist,
    }

    return render(request, 'curo/orderdetail.html', context)


def updateOrder(request):
    """ Update the order form """

    contractors = Contractors.objects.all()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    abort_save = 0

    if request.GET:
        if 'order_number' in request.GET:
            orderno = request.GET['order_number']
            thisorder = Orders.objects.get(orderNumber=orderno)
            thisnotification = Notifications(orderNumber=orderno,
                                             readUnread=0)
    else:
        messages.success(request, 'Oops! Something went wrong.')
        orderlist = Orders.objects.all().order_by('-orderNumber')
        order_list_length = orderlist.count()

        context = {
            'orderlist': orderlist,
            'order_list_length': order_list_length,
            'uploadlist': uploadlist,
        }

        return render(request, 'curo/orderlist.html', context)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=thisorder)
        """ validate the form data """
        validate_orderDescription = form.data['orderDescription']
        if not re.match("^[a-zA-Z ]+$", ''.join(validate_orderDescription)):
            messages.success(request, mark_safe('There was a problem with \
                    orderDescription.'))
            abort_save = 1
        validate_name = form.data['name']
        if not re.match("^[a-z A-Z?:',.-]+$", ''.join(validate_name)):
            messages.success(request, mark_safe('There was a problem with \
                    name.'))
            abort_save = 1
        validate_address = form.data['address']
        if not re.match("^[0-9 a-z A-Z?:',.-]+$", ''.join(validate_address)):
            messages.success(request, mark_safe('There was a problem with \
                    address.'))
            abort_save = 1
        validate_contact = form.data['contact']
        if not re.match("^[0-9]+$", ''.join(validate_contact)):
            messages.success(request, mark_safe('There was a problem with \
                    Contact.'))
            abort_save = 1
        validate_appointmentDate = form.data['appointmentDate']
        if len(validate_appointmentDate) > 0:
            if not re.match("^[0-9 :-]+$", ''.join(validate_appointmentDate)):
                messages.success(request, mark_safe('There was a problem with \
                        Appointment Date.'))
                abort_save = 1
        validate_dateClosed = form.data['dateClosed']
        if len(validate_dateClosed) > 0:
            if not re.match("^[0-9 :-]+$", ''.join(validate_dateClosed)):
                messages.success(request, mark_safe('There was a problem with \
                        Date Closed.'))
                abort_save = 1
        validate_notes = form.data['notes']
        if validate_notes != "":
            if not re.match("^[0-9 a-z A-Z?:@',|.-]+$", ''.join(validate_notes)):
                messages.success(request, mark_safe('There was a problem with \
                        notes.'))
                abort_save = 1
        if abort_save != 1:
            if form.is_valid():
                thisnotification.save()
                form.save()
    else:
        messages.success(request, 'Order not valid.')
        orderlist = Orders.objects.all().order_by('-orderNumber')
        order_list_length = orderlist.count()

        context = {
            'orderlist': orderlist,
            'order_list_length': order_list_length,
            'uploadlist': uploadlist,
        }

        return render(request, 'curo/orderlist.html', context)

    context = {
        'orderno': orderno,
        'form': form,
        'order_list_length': '1',
        'contractors': contractors,
        'uploadlist': uploadlist,
    }

    return render(request, 'curo/orderdetail.html', context)


def createOrder(request):
    """ Create a new order """

    contractors = Contractors.objects.all()
    form = OrderForm()
    page = 'ordernew'

    context = {
        'form': form,
        'contractors': contractors,
        'page': page,
    }

    return render(request, 'curo/ordernew.html', context)


def saveOrder(request):
    """ Save the new order """

    abort_save = 0

    if request.method == 'POST':
        form = OrderForm(request.POST)
        """ validate the form data """
        validate_orderDescription = form.data['orderDescription']
        if not re.match("^[a-zA-Z ]+$", ''.join(validate_orderDescription)):
            messages.success(request, mark_safe('There was a problem with \
                    orderDescription.'))
            abort_save = 1
        validate_name = form.data['name']
        if not re.match("^[a-z A-Z?:',.-]+$", ''.join(validate_name)):
            messages.success(request, mark_safe('There was a problem with \
                    name.'))
            abort_save = 1
        validate_address = form.data['address']
        if not re.match("^[0-9 a-z A-Z?:',.-]+$", ''.join(validate_address)):
            messages.success(request, mark_safe('There was a problem with \
                    address.'))
            abort_save = 1
        validate_notes = form.data['notes']
        if validate_notes != "":
            if not re.match("^[0-9 a-z A-Z?:@',|.-]+$", ''.join(validate_notes)):
                messages.success(request, mark_safe('There was a problem with \
                        notes.'))
                abort_save = 1

        """ check if that OrderNumber already exists """
        orders = Orders.objects.all()
        this_order = form.data['orderNumber']
        order_exists = (orders.filter
                        (orderNumber=this_order))
        thisnotification = Notifications(orderNumber=this_order,
                                         readUnread=0)
        if order_exists:
            messages.success(request, 'That Order Number already exists!')
        else:
            if abort_save != 1:
                if form.is_valid():
                    thisnotification.save()
                    form.save()
                else:
                    messages.success(request, 'Order not valid.')
    else:
        messages.success(request, 'Oops! Something went awry.')

    orderlist = Orders.objects.all().order_by('-orderNumber')
    order_list_length = orderlist.count()

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
    }

    return render(request, 'curo/orderlist.html', context)


def searchOrders(request):
    """ A view to return a list of orders that meet the search criteria """

    orderlist = Orders.objects.all().order_by('-orderNumber')
    order_list_length = orderlist.count()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    searchstring = ""

    if request.GET:
        if 'search_string' in request.GET:
            searchstring = request.GET['search_string']
            if len(searchstring) != 0:
                if not re.match("^[0-9 a-z A-Z?:@',|.-]+$", ''.join(searchstring)):
                    messages.success(request,
                                     mark_safe('There was a problem with  \
                                                search'))
            queries = (Q(orderNumber__icontains=searchstring) |
                       Q(orderDescription__icontains=searchstring) |
                       Q(name__icontains=searchstring) |
                       Q(address__icontains=searchstring) |
                       Q(contractor__contractor__icontains=searchstring) |
                       Q(primaryContact__username__icontains=searchstring) |
                       Q(secondaryContact__icontains=searchstring) |
                       Q(notes__icontains=searchstring))
            orders = Orders.objects.all()
            orderlist = (orders.filter(queries)
                         .order_by('-orderNumber'))
            order_list_length = orders.filter(queries).count()
    else:
        messages.success(request, 'Oops! Something went wrong.')

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
        'searchstring': searchstring,
        'uploadlist': uploadlist,
    }

    return render(request, 'curo/orderlist.html', context)


def orderOrders(request):
    """ A view to order the orders by a selected field """

    orderlist = Orders.objects.all()
    order_list_length = orderlist.count()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    searchstring = ""

    if request.GET:
        if 'searchstring' in request.GET:
            searchstring = request.GET['searchstring']
            queries = (Q(orderNumber__icontains=searchstring) |
                       Q(orderDescription__icontains=searchstring) |
                       Q(name__icontains=searchstring) |
                       Q(address__icontains=searchstring) |
                       Q(contractor__contractor__icontains=searchstring) |
                       Q(primaryContact__username__icontains=searchstring) |
                       Q(secondaryContact__icontains=searchstring) |
                       Q(notes__icontains=searchstring))
            orders = Orders.objects.all()
            orderlist = (orders.filter(queries))
            order_list_length = orderlist.count()

        if 'searchorder' in request.GET:
            searchorder = request.GET['searchorder']

        if 'order_field' in request.GET:
            orderfield = request.GET['order_field']
            if orderfield == 'orderNumber':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('orderNumber')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-orderNumber')
            if orderfield == 'orderDescription':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('orderDescription')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-orderDescription')
            if orderfield == 'name':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('name')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-name')
            if orderfield == 'address':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('address')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-address')
            if orderfield == 'contractor':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('contractor')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-contractor')
            if orderfield == 'appointmentDate':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('appointmentDate')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-appointmentDate')
            if orderfield == 'primaryContact':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('primaryContact')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-primaryContact')
            if orderfield == 'secondaryContact':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('secondaryContact')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-secondaryContact')
            if orderfield == 'notes':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('notes')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-notes')
            if orderfield == 'dateLastUpdate':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('dateLastUpdate')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-dateLastUpdate')
            if orderfield == 'dateCreated':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('dateCreated')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-dateCreated')
    else:
        messages.success(request, 'Oops! Something went wrong.')

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
        'searchstring': searchstring,
        'uploadlist': uploadlist,
    }

    return render(request, 'curo/orderlist.html', context)


def dashboard(request, guage):
    """ A view to return the dashboard """

    orders = Orders.objects.all()
    notifications = Notifications.objects.all()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    distinctUploads = UploadFile.objects.values('orderNumber').distinct()

    if guage == 'open':
        queries = ((Q(primaryContact__username__icontains=request.user.username) |
                   Q(secondaryContact__icontains=request.user.username)) &
                   Q(appointmentDate__isnull=True))
    elif guage == 'appt':
        queries = ((Q(primaryContact__username__icontains=request.user.username) |
                   Q(secondaryContact__icontains=request.user.username)) &
                   Q(appointmentDate__isnull=False) &
                   Q(appointmentComplete__icontains='No'))
    elif guage == 'past':
        queries = ((Q(primaryContact__username__icontains=request.user.username) |
                   Q(secondaryContact__icontains=request.user.username)) &
                   Q(appointmentDate__isnull=False) &
                   Q(appointmentComplete__icontains='No'))
    elif guage == 'comp':
        queries = ((Q(primaryContact__username__icontains=request.user.username) |
                   Q(secondaryContact__icontains=request.user.username)) &
                   Q(appointmentDate__isnull=False) &
                   Q(appointmentComplete__icontains='Yes'))
    elif guage == 'repo':
        queries = ((Q(primaryContact__username__icontains=request.user.username) |
                   Q(secondaryContact__icontains=request.user.username)) &
                   Q(appointmentDate__isnull=False))
    elif guage == 'clsd':
        queries = ((Q(primaryContact__username__icontains=request.user.username) |
                   Q(secondaryContact__icontains=request.user.username)) &
                   Q(appointmentDate__isnull=False) &
                   Q(appointmentComplete__icontains='Yes') &
                   Q(dateClosed__isnull=False))
    else:
        queries = (Q(primaryContact__username__icontains=request.user.username) |
                   Q(secondaryContact__icontains=request.user.username))
    orders = Orders.objects.all()
    orderlist = (orders.filter(queries)
                 .order_by('-dateLastUpdate'))
    order_list_length = orders.filter(queries).count()
    page = 'dashboard'
    comparedate = timezone.now()

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
        'notifications': notifications,
        'page': page,
        'guage': guage,
        'comparedate': comparedate,
        'uploadlist': uploadlist,
        'distinctUploads': distinctUploads,
    }

    return render(request, 'curo/dashboard.html', context)


def searchDashboard(request, guage):
    """ A view to return a list of orders that meet the search criteria """

    orderlist = Orders.objects.all().order_by('-orderNumber')
    order_list_length = orderlist.count()
    searchstring = ""
    notifications = Notifications.objects.all()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    distinctUploads = UploadFile.objects.values('orderNumber').distinct()
    page = 'dashboard'

    if request.GET:
        if 'search_string' in request.GET:
            searchstring = request.GET['search_string']
            if len(searchstring) != 0:
                if not re.match("^[0-9 a-z A-Z?:@',|.-]+$", ''.join(searchstring)):
                    messages.success(request,
                                     mark_safe('There was a problem with  \
                                                search'))
    else:
        messages.success(request, 'Oops! Something went wrong.')

    if guage == 'open':
        queries = (
                   (Q(primaryContact__username__icontains=request.user.username) |
                    Q(secondaryContact__icontains=request.user.username)) &
                   (Q(appointmentDate__isnull=True)) &
                   (Q(orderNumber__icontains=searchstring) |
                    Q(orderDescription__icontains=searchstring) |
                    Q(name__icontains=searchstring) |
                    Q(address__icontains=searchstring) |
                    Q(contractor__contractor__icontains=searchstring) |
                    Q(notes__icontains=searchstring))
                   )
    elif guage == 'appt':
        queries = (
                   (Q(primaryContact__username__icontains=request.user.username) |
                    Q(secondaryContact__icontains=request.user.username)) &
                   (Q(appointmentDate__isnull=False) &
                    Q(appointmentComplete__icontains='No')) &
                   (Q(orderNumber__icontains=searchstring) |
                    Q(orderDescription__icontains=searchstring) |
                    Q(name__icontains=searchstring) |
                    Q(address__icontains=searchstring) |
                    Q(contractor__contractor__icontains=searchstring) |
                    Q(notes__icontains=searchstring))
                    )
    elif guage == 'past':
        queries = (
                   (Q(primaryContact__username__icontains=request.user.username) |
                    Q(secondaryContact__icontains=request.user.username)) &
                   (Q(appointmentDate__isnull=False) &
                    Q(appointmentComplete__icontains='No')) &
                   (Q(orderNumber__icontains=searchstring) |
                    Q(orderDescription__icontains=searchstring) |
                    Q(name__icontains=searchstring) |
                    Q(address__icontains=searchstring) |
                    Q(contractor__contractor__icontains=searchstring) |
                    Q(notes__icontains=searchstring))
                   )
    elif guage == 'comp':
        queries = (
                   (Q(primaryContact__username__icontains=request.user.username) |
                    Q(secondaryContact__icontains=request.user.username)) &
                   (Q(appointmentDate__isnull=False) &
                    Q(appointmentComplete__icontains='Yes')) &
                   (Q(orderNumber__icontains=searchstring) |
                    Q(orderDescription__icontains=searchstring) |
                    Q(name__icontains=searchstring) |
                    Q(address__icontains=searchstring) |
                    Q(contractor__contractor__icontains=searchstring) |
                    Q(notes__icontains=searchstring))
                   )
    elif guage == 'repo':
        queries = (
                   (Q(primaryContact__username__icontains=request.user.username) |
                    Q(secondaryContact__icontains=request.user.username)) &
                   (Q(appointmentDate__isnull=False)) &
                   (Q(orderNumber__icontains=searchstring) |
                    Q(orderDescription__icontains=searchstring) |
                    Q(name__icontains=searchstring) |
                    Q(address__icontains=searchstring) |
                    Q(contractor__contractor__icontains=searchstring) |
                    Q(notes__icontains=searchstring))
                   )
    elif guage == 'clsd':
        queries = (
                   (Q(primaryContact__username__icontains=request.user.username) |
                    Q(secondaryContact__icontains=request.user.username)) &
                   (Q(appointmentDate__isnull=False) &
                    Q(appointmentComplete__icontains='Yes') &
                    Q(dateClosed__isnull=False)) &
                   (Q(orderNumber__icontains=searchstring) |
                    Q(orderDescription__icontains=searchstring) |
                    Q(name__icontains=searchstring) |
                    Q(address__icontains=searchstring) |
                    Q(contractor__contractor__icontains=searchstring) |
                    Q(notes__icontains=searchstring))
                   )
    else:
        queries = (
                   (Q(primaryContact__username__icontains=request.user.username) |
                    Q(secondaryContact__icontains=request.user.username)) &
                   (Q(orderNumber__icontains=searchstring) |
                    Q(orderDescription__icontains=searchstring) |
                    Q(name__icontains=searchstring) |
                    Q(address__icontains=searchstring) |
                    Q(contractor__contractor__icontains=searchstring) |
                    Q(notes__icontains=searchstring))
                   )
    orders = Orders.objects.all()
    orderlist = (orders.filter(queries)
                 .order_by('-dateLastUpdate'))
    order_list_length = orders.filter(queries).count()
    comparedate = timezone.now()

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
        'searchstring': searchstring,
        'notifications': notifications,
        'page': page,
        'guage': guage,
        'comparedate': comparedate,
        'uploadlist': uploadlist,
        'distinctUploads': distinctUploads,
    }

    return render(request, 'curo/dashboard.html', context)


def orderDashboard(request, guage):
    """ A view to order the orders by a selected field """

    orderlist = Orders.objects.all()
    order_list_length = orderlist.count()
    searchstring = ""
    notifications = Notifications.objects.all()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')
    distinctUploads = UploadFile.objects.values('orderNumber').distinct()
    page = 'dashboard'
    comparedate = timezone.now()

    if request.GET:
        if 'searchstring' in request.GET:
            searchstring = request.GET['searchstring']
            if guage == 'open':
                queries = (
                           (Q(primaryContact__username__icontains=request.user.username) |
                            Q(secondaryContact__icontains=request.user.username)) &
                           (Q(appointmentDate__isnull=True)) &
                           (Q(orderNumber__icontains=searchstring) |
                            Q(orderDescription__icontains=searchstring) |
                            Q(name__icontains=searchstring) |
                            Q(address__icontains=searchstring) |
                            Q(contractor__contractor__icontains=searchstring) |
                            Q(notes__icontains=searchstring))
                           )
            elif guage == 'appt':
                queries = (
                           (Q(primaryContact__username__icontains=request.user.username) |
                            Q(secondaryContact__icontains=request.user.username)) &
                           (Q(appointmentDate__isnull=False) &
                            Q(appointmentComplete__icontains='No')) &
                           (Q(orderNumber__icontains=searchstring) |
                            Q(orderDescription__icontains=searchstring) |
                            Q(name__icontains=searchstring) |
                            Q(address__icontains=searchstring) |
                            Q(contractor__contractor__icontains=searchstring) |
                            Q(notes__icontains=searchstring))
                           )
            elif guage == 'past':
                queries = (
                           (Q(primaryContact__username__icontains=request.user.username) |
                            Q(secondaryContact__icontains=request.user.username)) &
                           (Q(appointmentDate__isnull=False) &
                            Q(appointmentComplete__icontains='No')) &
                           (Q(orderNumber__icontains=searchstring) |
                            Q(orderDescription__icontains=searchstring) |
                            Q(name__icontains=searchstring) |
                            Q(address__icontains=searchstring) |
                            Q(contractor__contractor__icontains=searchstring) |
                            Q(notes__icontains=searchstring))
                           )
            elif guage == 'comp':
                queries = (
                           (Q(primaryContact__username__icontains=request.user.username) |
                            Q(secondaryContact__icontains=request.user.username)) &
                           (Q(appointmentDate__isnull=False) &
                            Q(appointmentComplete__icontains='Yes')) &
                           (Q(orderNumber__icontains=searchstring) |
                            Q(orderDescription__icontains=searchstring) |
                            Q(name__icontains=searchstring) |
                            Q(address__icontains=searchstring) |
                            Q(contractor__contractor__icontains=searchstring) |
                            Q(notes__icontains=searchstring))
                           )
            elif guage == 'repo':
                queries = (
                           (Q(primaryContact__username__icontains=request.user.username) |
                            Q(secondaryContact__icontains=request.user.username)) &
                           (Q(appointmentDate__isnull=False)) &
                           (Q(orderNumber__icontains=searchstring) |
                            Q(orderDescription__icontains=searchstring) |
                            Q(name__icontains=searchstring) |
                            Q(address__icontains=searchstring) |
                            Q(contractor__contractor__icontains=searchstring) |
                            Q(notes__icontains=searchstring))
                           )
            elif guage == 'clsd':
                queries = (
                           (Q(primaryContact__username__icontains=request.user.username) |
                            Q(secondaryContact__icontains=request.user.username)) &
                           (Q(appointmentDate__isnull=False) &
                            Q(appointmentComplete__icontains='Yes') &
                            Q(dateClosed__isnull=False)) &
                           (Q(orderNumber__icontains=searchstring) |
                            Q(orderDescription__icontains=searchstring) |
                            Q(name__icontains=searchstring) |
                            Q(address__icontains=searchstring) |
                            Q(contractor__contractor__icontains=searchstring) |
                            Q(notes__icontains=searchstring))
                           )
            else:
                queries = (
                           (Q(primaryContact__username__icontains=request.user.username) |
                            Q(secondaryContact__icontains=request.user.username)) &
                           (Q(orderNumber__icontains=searchstring) |
                            Q(orderDescription__icontains=searchstring) |
                            Q(name__icontains=searchstring) |
                            Q(address__icontains=searchstring) |
                            Q(contractor__contractor__icontains=searchstring) |
                            Q(notes__icontains=searchstring))
                           )
            orders = Orders.objects.all()
            orderlist = (orders.filter(queries)
                         .order_by('-dateLastUpdate'))
            order_list_length = orders.filter(queries).count()

        if 'searchorder' in request.GET:
            searchorder = request.GET['searchorder']

        if 'order_field' in request.GET:
            orderfield = request.GET['order_field']
            if orderfield == 'orderNumber':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('orderNumber')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-orderNumber')
            if orderfield == 'orderDescription':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('orderDescription')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-orderDescription')
            if orderfield == 'name':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('name')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-name')
            if orderfield == 'address':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('address')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-address')
            if orderfield == 'contractor':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('contractor')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-contractor')
            if orderfield == 'appointmentDate':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('appointmentDate')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-appointmentDate')
            if orderfield == 'primaryContact':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('primaryContact')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-primaryContact')
            if orderfield == 'secondaryContact':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('secondaryContact')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-secondaryContact')
            if orderfield == 'notes':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('notes')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-notes')
            if orderfield == 'dateLastUpdate':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('dateLastUpdate')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-dateLastUpdate')
            if orderfield == 'dateCreated':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('dateCreated')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-dateCreated')
            if orderfield == 'dateClosed':
                if searchorder == 'az':
                    orderlist = orderlist.order_by('dateClosed')
                if searchorder == 'za':
                    orderlist = orderlist.order_by('-dateClosed')
    else:
        messages.success(request, 'Oops! Something went wrong.')

    context = {
        'orderlist': orderlist,
        'order_list_length': order_list_length,
        'searchstring': searchstring,
        'notifications': notifications,
        'page': page,
        'guage': guage,
        'comparedate': comparedate,
        'uploadlist': uploadlist,
        'distinctUploads': distinctUploads,
    }

    return render(request, 'curo/dashboard.html', context)


def selectNotification(request, orderno):
    """ Update the order form """

    orders = Orders.objects.all()
    this_order = Orders.objects.get(orderNumber=orderno)
    order_list_length = orders.filter(orderNumber=orderno).count()
    form = OrderForm(instance=this_order)
    contractors = Contractors.objects.all()
    uploadlist = UploadFile.objects.all().order_by('-dateUploaded')

    thisnotification = Notifications(orderNumber=orderno,
                                     readUnread=1)
    thisnotification.save()

    context = {
        'orderno': orderno,
        'form': form,
        'order_list_length': order_list_length,
        'contractors': contractors,
        'uploadlist': uploadlist,
    }

    return render(request, 'curo/orderdetail.html', context)
