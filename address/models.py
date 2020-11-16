from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class AddressModel(models.Model):
    address = models.FileField(upload_to='documents/',validators=[FileExtensionValidator(allowed_extensions=['xlsx'])])

