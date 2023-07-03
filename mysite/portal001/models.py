from django.db import models

# Create your models here.


class Orders(models.Model):

    class Meta:
        verbose_name_plural = 'Orders'

    orderNumber = models.DecimalField(max_digits=10, decimal_places=0, null=False)
    orderDescription = models.CharField(max_length=254, null=False)
    name = models.CharField(max_length=254, null=False)
    address = models.CharField(max_length=254, null=False)
    contractor = models.CharField(max_length=254, null=False)
    appointmentDate = models.DateField()
    primaryContact = models.EmailField(max_length=254)
    secondaryContact = models.EmailField(max_length=254)
    notes = models.CharField(max_length=254, null=True)
    dateLastUpdate = models.DateField()

    def __str__(self):
        return str(int(self.orderNumber))
