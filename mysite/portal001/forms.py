# Credit: Code-Institute
from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('orderNumber', 'orderDescription', 'name',
                  'address', 'contractor',
                  'appointmentDate', 'primaryContact', 'secondaryContact',
                  'notes', 'dateLastUpdate', 'dateCreated',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'orderNumber': 'Order Number',
            'orderDescription': 'Order Description',
            'name': 'Name',
            'address': 'Address',
            'contractor': 'Contractor',
            'appointmentDate': 'Appointment Date',
            'primaryContact': 'Primary Contact',
            'secondaryContact': 'Secondary Contact',
            'notes': 'Notes',
            'dateLastUpdate': 'Last Updated',
            'dateCreated': 'Date Created',
        }
