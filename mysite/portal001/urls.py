from django.urls import path
from . import views

urlpatterns = [
    path('', views.curo, name='curo'),
    path('selectOrder/<orderno>', views.selectOrder, name='selectOrder'),
    path('updateOrder', views.updateOrder, name='updateOrder'),
    path('createOrder', views.createOrder, name='createOrder'),
    path('searchOrders/<searchstr>', views.searchOrders, name='searchOrders'),
]
