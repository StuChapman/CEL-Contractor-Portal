from django.db import models

# Create your models here.


class UploadFile(models.Model):

    class Meta:
        verbose_name_plural = 'UploadFile'

    orderNumber = models.DecimalField(max_digits=10, decimal_places=0,
                                      null=False, primary_key=True)
    uploadFile = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(int(self.orderNumber))
