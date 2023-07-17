from django.urls import path
from . import views

urlpatterns = [
    path('', views.curoContractors, name='curoContractors'),
    path('searchContractors',
         views.searchContractors, name='searchContractors'),
    path('orderContractors', views.orderContractors, name='orderContractors'),
    path('selectContractor/<contractor>',
         views.selectContractor, name='selectContractor'),
    path('newContractor', views.newContractor, name='newContractor'),
    path('saveNewContractor', views.saveNewContractor, name='saveNewContractor'),
]
