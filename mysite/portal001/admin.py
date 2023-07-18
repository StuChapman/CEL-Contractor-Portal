from django.contrib import admin

# Register your models here.

from .models import Orders, Contractors, Notifications

admin.site.register(Orders)
admin.site.register(Contractors)
admin.site.register(Notifications)
