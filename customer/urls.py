from ticket.views import customer_popup
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import *

urlpatterns = [
    path('customer-create/',customer_popup, name='customer-popup')
]