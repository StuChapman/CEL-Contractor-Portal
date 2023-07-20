from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class Orders(models.Model):

    class Meta:
        verbose_name_plural = 'Orders'

    APPT_COMP_CHOICES = [
        ("No", "No"),
        ("Yes", "Yes"),
    ]

    orderNumber = models.DecimalField(max_digits=10, decimal_places=0,
                                      null=False, primary_key=True)
    orderDescription = models.CharField(max_length=254, null=False)
    name = models.CharField(max_length=254, null=False)
    address = models.CharField(max_length=254, null=False)
    contact = models.CharField(max_length=254, null=False, default=0)
    contractor = models.ForeignKey('Contractors',
                                   on_delete=models.CASCADE,
                                   to_field='contractor',
                                   related_name='name')
    appointmentDate = models.DateTimeField(null=True, blank=True)
    appointmentComplete = models.CharField(max_length=3,
                                           choices=APPT_COMP_CHOICES,
                                           default="No",)
    primaryContact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE)
    secondaryContact = models.EmailField(max_length=254)
    notes = models.CharField(max_length=9999, null=True, blank=True)
    dateLastUpdate = models.DateTimeField(default=timezone.now)
    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(int(self.orderNumber))


class Contractors(models.Model):

    class Meta:
        verbose_name_plural = 'Contractors'

    contractor = models.CharField(max_length=254, null=False, primary_key=True)
    secondaryContact = models.EmailField(max_length=254, unique=True)
    services = models.CharField(max_length=9999, null=True, blank=True)

    def __str__(self):
        return str(self.contractor)


class Notifications(models.Model):

    class Meta:
        verbose_name_plural = 'Notifications'

    orderNumber = models.DecimalField(max_digits=10, decimal_places=0,
                                      null=False, primary_key=True)
    readUnread = models.DecimalField(max_digits=1, decimal_places=0, default=0)

    def __str__(self):
        return str(int(self.orderNumber))
