from django.urls import path,include
from .views import process_address
urlpatterns = [
    path('',process_address),
]
