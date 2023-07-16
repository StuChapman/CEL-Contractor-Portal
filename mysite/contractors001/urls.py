from django.urls import path
from . import views

urlpatterns = [
    path('', views.curoContractors, name='curoContractors'),
    path('searchContractors',
         views.searchContractors, name='searchContractors'),
    path('orderContractors', views.orderContractors, name='orderContractors'),
    path('selectContractor/<contractor>',
         views.selectContractor, name='selectContractor'),
    path('updateContractor', views.updateContractor, name='updateContractor'),
]
