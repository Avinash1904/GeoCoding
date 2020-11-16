from django import forms
from .models import AddressModel
from .service import service
class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = ('address',)
    
