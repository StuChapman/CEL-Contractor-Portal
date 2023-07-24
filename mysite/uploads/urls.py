from django.urls import path
from . import views

urlpatterns = [
    path('uploadFile/<orderno>', views.uploadFile, name='uploadFile'),
    path('upload_file', views.upload_file, name='upload_file'),
]
