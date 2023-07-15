# Credit: Code-Institute
from django import forms
from portal001.models import Contractors


class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractors
        fields = ('contractor', 'secondaryContact',
                  'services',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'contractor': 'Contractor',
            'secondaryContact': 'Secondary Contact',
            'services': 'Services',
        }
