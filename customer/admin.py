from django.contrib import admin
from .models import *

# Customer Admin
# Register your models here.

admin.site.register(Company)
admin.site.register(Customer)
admin.site.register(Jobsite)