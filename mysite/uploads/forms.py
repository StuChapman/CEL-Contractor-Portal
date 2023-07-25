from django import forms
from .models import UploadFile


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('orderNumber', 'uploadFile',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_orderNumber': 'orderNumber',
            'default_uploadFile': 'uploadFile',
        }
