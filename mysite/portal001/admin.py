from django.contrib import admin

# Register your models here.

from .models import Orders, Contractors

admin.site.register(Orders)
admin.site.register(Contractors)
