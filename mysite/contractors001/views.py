from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import path
from django.contrib import messages
from . import views
from portal001.models import Contractors
from .forms import ContractorForm
from django.db.models import Q
from django.utils import timezone
from django.utils.safestring import mark_safe
import re


def curoContractors(request):
    """ A view to return the intro page """

    contractorlist = Contractors.objects.all().order_by('contractor')
    contractor_list_length = contractorlist.count()
    page = 'contractorlist'

    context = {
        'contractorlist': contractorlist,
        'contractor_list_length': contractor_list_length,
        'page': page,
    }

    return render(request, 'curo/contractorlist.html', context)


def searchContractors(request):
    """ A view to return a list of contractors that meet the search criteria """

    contractorlist = Contractors.objects.all().order_by('contractor')
    contractor_list_length = contractorlist.count()
    searchstring = ""

    if request.GET:
        if 'search_string' in request.GET:
            searchstring = request.GET['search_string']
            if len(searchstring) != 0:
                if not re.match("^[0-9 a-z A-Z?:@',|.-]+$", ''.join(searchstring)):
                    messages.success(request,
                                     mark_safe('There was a problem with  \
                                                search'))
            queries = (Q(contractor__icontains=searchstring) |
                       Q(secondaryContact__icontains=searchstring) |
                       Q(services__icontains=searchstring))
            contractors = Contractors.objects.all()
            contractorlist = (contractors.filter(queries)
                              .order_by('contractor'))
            contractor_list_length = contractors.filter(queries).count()
    else:
        messages.success(request, 'Oops! Something went wrong.')

    context = {
        'contractorlist': contractorlist,
        'contractor_list_length': contractor_list_length,
        'searchstring': searchstring,
    }

    return render(request, 'curo/contractorlist.html', context)


def orderContractors(request):
    """ A view to order the contractors by a selected field """

    contractorlist = Contractors.objects.all()
    contractor_list_length = contractorlist.count()
    searchstring = ""

    if request.GET:
        if 'searchstring' in request.GET:
            searchstring = request.GET['searchstring']
            queries = (Q(contractor__icontains=searchstring) |
                       Q(secondaryContact__icontains=searchstring) |
                       Q(services__icontains=searchstring))
            contractors = Contractors.objects.all()
            contractorlist = (contractors.filter(queries))
            contractor_list_length = contractorlist.count()
        
        if 'searchorder' in request.GET:
            searchorder = request.GET['searchorder']

        if 'order_field' in request.GET:
            orderfield = request.GET['order_field']
            if orderfield == 'contractor':
                if searchorder == 'az':
                    contractorlist = contractorlist.order_by('contractor')
                if searchorder == 'za':
                    contractorlist = contractorlist.order_by('-contractor')
            if orderfield == 'secondaryContact':
                if searchorder == 'az':
                    contractorlist = contractorlist.order_by('secondaryContact')
                if searchorder == 'za':
                    contractorlist = contractorlist.order_by('-secondaryContact')
            if orderfield == 'notes':
                if searchorder == 'az':
                    contractorlist = contractorlist.order_by('services')
                if searchorder == 'za':
                    contractorlist = contractorlist.order_by('-services')
    else:
        messages.success(request, 'Oops! Something went wrong.')

    context = {
        'contractorlist': contractorlist,
        'contractor_list_length': contractor_list_length,
        'searchstring': searchstring,
    }

    return render(request, 'curo/contractorlist.html', context)


def selectContractor(request, contractor):
    """ Update the order form """

    contractors = Contractors.objects.all()
    contractorlist = 1
    this_contractor = Contractors.objects.get(contractor=contractor)
    contractor_list_length = contractors.filter(contractor=contractor).count()
    form = ContractorForm(instance=this_contractor)
    contractors = Contractors.objects.all()
    page = 'contractordetail'

    context = {
        'contractorlist': contractorlist,
        'contractor': contractor,
        'form': form,
        'contractor_list_length': contractor_list_length,
        'contractors': contractors,
        'page': page,
    }

    return render(request, 'curo/contractordetail.html', context)


def updateContractor(request):
    """ Update the order form """

    contractors = Contractors.objects.all()
    abort_save = 0

    if request.GET:
        if 'contractor' in request.GET:
            contractor = request.GET['contractor']
            thiscontractor = Contractors.objects.get(contractor=contractor)
    else:
        messages.success(request, 'Oops! Something went wrong.')
        contractorlist = Contractors.objects.all().order_by('contractor')
        contractor_list_length = contractorlist.count()

        context = {
            'contractorlist': contractorlist,
            'contractor_list_length': contractor_list_length,
        }

        return render(request, 'curo/orderlist.html', context)

    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=thiscontractor)
        """ validate the form data """
        validate_secondaryContact = form.data['secondaryContact']
        if not re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$", ''.join(validate_secondaryContact)):
            messages.success(request, mark_safe('There was a problem with \
                    secondaryContact.'))
            abort_save = 1
        validate_services = form.data['services']
        if validate_services != "":
            if not re.match("^[0-9 a-z A-Z?:@',|.-]+$", ''.join(validate_services)):
                messages.success(request, mark_safe('There was a problem with \
                        Services.'))
                abort_save = 1
        if abort_save != 1:
            if form.is_valid():
                form.save()
    else:
        messages.success(request, 'Contractor not valid.')
        contractorlist = Contractors.objects.all().order_by('contractor')
        contractor_list_length = contractorlist.count()

        context = {
            'contractorlist': contractorlist,
            'contractor_list_length': contractor_list_length,
        }

        return render(request, 'curo/contractorlist.html', context)

    context = {
        'contractor': contractor,
        'form': form,
        'contractor_list_length': '1',
        'contractors': contractors,
    }

    return render(request, 'curo/contractordetail.html', context)


def newContractor(request):
    """ Create a new contractor """

    contractors = Contractors.objects.all()
    form = ContractorForm()
    contractorlist = 1
    page = 'contractornew'

    context = {
        'form': form,
        'contractors': contractors,
        'contractorlist': contractorlist,
        'page': page,
    }

    return render(request, 'curo/contractornew.html', context)


def saveNewContractor(request):
    """ Save the new order """

    abort_save = 0

    if request.method == 'POST':
        form = ContractorForm(request.POST)
        """ validate the form data """
        validate_contractor = form.data['contractor']
        if not re.match("^[0-9 a-z A-Z?:@',|.-]+$", ''.join(validate_contractor)):
            messages.success(request, mark_safe('There was a problem with \
                                                 Contractor.'))
            abort_save = 1
        validate_secondaryContact = form.data['secondaryContact']
        if not re.match("^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$",
                        ''.join(validate_secondaryContact)):
            messages.success(request, mark_safe('There was a problem with \
                    secondaryContact.'))
            abort_save = 1
        validate_services = form.data['services']
        if not re.match("^[0-9 a-z A-Z?:@',|.-]+$",
                        ''.join(validate_services)):
            messages.success(request, mark_safe('There was a problem with \
                    Services.'))
            abort_save = 1

        """ check if that Contractor already exists """
        contractors = Contractors.objects.all()
        this_contractor = form.data['contractor']
        contractor_exists = (contractors.filter
                        (contractor=this_contractor))
        if contractor_exists:
            messages.success(request, 'That Contractor Number already exists!')
        else:
            if abort_save != 1:
                if form.is_valid():
                    form.save()
                else:
                    messages.success(request, 'Contractor not valid.')
    else:
        messages.success(request, 'Oops! Something went awry.')

    contractorlist = Contractors.objects.all().order_by('contractor')
    contractor_list_length = contractorlist.count()

    context = {
        'contractorlist': contractorlist,
        'contractor_list_length': contractor_list_length,
    }

    return render(request, 'curo/contractorlist.html', context)
