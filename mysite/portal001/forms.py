# Credit: Code-Institute
from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('orderNumber', 'orderDescription', 'name',
                  'address', 'contact', 'contractor',
                  'appointmentDate', 'appointmentComplete',
                  'primaryContact', 'secondaryContact',
                  'notes', 'dateLastUpdate', 'dateCreated',
                  'dateClosed',)

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
            'contact': 'Contact',
            'contractor': 'Contractor',
            'appointmentDate': 'Appointment Date',
            'appointmentComplete': 'Appointment Complete',
            'primaryContact': 'Primary Contact',
            'secondaryContact': 'Secondary Contact',
            'notes': 'Notes',
            'dateLastUpdate': 'Last Updated',
            'dateCreated': 'Date Created',
            'dateClosed': 'Date Closed',
        }
