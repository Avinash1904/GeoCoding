from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from .forms import AddressForm
from .service import service
# Create your views here.

def process_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            # alter the file accordingly
            proceessed = service.process_geo_location(instance.address.name)
            if not proceessed:
                instance.delete()
                raise ValidationError("Not a valid excel file")
            return render(request,'download.html',{'instance':instance})

    else:
        form = AddressForm()
    return render(request, 'form.html', {'form': form})