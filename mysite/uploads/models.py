from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator

# Create your models here.


class UploadFile(models.Model):

    class Meta:
        verbose_name_plural = 'UploadFile'

    id_no = models.AutoField(primary_key=True)
    orderNumber = models.DecimalField(max_digits=10, decimal_places=0,
                                      null=False)
    uploadFile = models.FileField(null=False,
                                  upload_to="media/uploadedfiles/",
                                  validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    dateUploaded = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(int(self.orderNumber))
