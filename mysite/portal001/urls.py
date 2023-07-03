from django.urls import path
from . import views

urlpatterns = [
    path('portal001/', views.curo, name='curo'),
]
