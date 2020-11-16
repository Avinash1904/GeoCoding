from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django import forms
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
                return render(request,'form.html',{'form':form,'error':'Not a valid Excel File','is_download_url':False})
            #     raise forms.ValidationError({
            # "address": "Not a valid excel file"})
                #raise ValidationError("Not a valid excel file")
            return render(request,'form.html',{'instance':instance,'error':None,'is_download_url':True})

    else:
        form = AddressForm()
    return render(request, 'form.html', {'form': form,'error':None,'is_download_url':False})