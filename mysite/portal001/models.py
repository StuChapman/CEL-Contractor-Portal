from django.db import models
from django.utils import timezone

# Create your models here.


class Orders(models.Model):

    class Meta:
        verbose_name_plural = 'Orders'

    orderNumber = models.DecimalField(max_digits=10, decimal_places=0, null=False, primary_key=True)
    orderDescription = models.CharField(max_length=254, null=False)
    name = models.CharField(max_length=254, null=False)
    address = models.CharField(max_length=254, null=False)
    contractor = models.CharField(max_length=254, null=False)
    appointmentDate = models.DateTimeField()
    primaryContact = models.EmailField(max_length=254)
    secondaryContact = models.EmailField(max_length=254)
    notes = models.CharField(max_length=9999, null=True)
    dateLastUpdate = models.DateTimeField()
    dateCreated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(int(self.orderNumber))
