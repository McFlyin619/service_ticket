from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField
from django.forms.widgets import CheckboxInput
from django.urls import reverse
from django.db import models

from customer.models import *
from accounts.models import AccountCompany, AccountUser


import datetime
from django.utils import timezone

# Create your models here.
STOP = (
    ('1st','1st'),
    ('2nd','2nd'),
    ('3rd','3rd'),
    ('4th','4th'),
    ('5th','5th'),
    ('6th','6th'),
    ('LUNCH','LUNCH')
)

# JOBSITE_DEFAULT = (
#     ('Same as Customer','Same as Customer')
# )
class TicketType(models.Model):
    name = models.CharField(max_length=100)

    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ticket_app:ticket_type_list")

class ServiceProvided(models.Model):
    name = models.CharField(max_length=100)

    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ticket_app:serviceprovided_list")

#  Create a function that automatically creates a jobsite that is Same on everything to allow there to be no jobsite but use customer address instead. then add customer address to Ticket Deatil page
# def set_default_jobsite():
#     return Ticket.objects.get_or_create(t_jobsite='Same as customer')[0]


class Ticket(models.Model):
    ticket_number = models.CharField(primary_key=True, max_length=10)
    t_customer = models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
    t_jobsite = models.ForeignKey(Jobsite, null=True, on_delete=models.SET_NULL)
    stop = models.CharField(choices=STOP, max_length=254, default='1st')
    assigned = models.ManyToManyField(AccountUser, blank=True)
    department = models.ForeignKey(ServiceProvided,null=True, on_delete=models.SET_NULL)
    t_type = models.ForeignKey(TicketType,null=True, on_delete=models.SET_NULL)
    scope = models.TextField()
    repair_notes = models.TextField(blank=True)
    # parts_used = models.ManyToManyField(Part, blank=True)
    parts_used = models.TextField()
    additional_work = models.TextField(blank=True)
    schedule = models.DateField(default=datetime.date.today)
    start_job = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    start_time = models.DateTimeField(blank=True,null=True)
    end_time = models.DateTimeField(blank=True,null=True)

    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # automatically assigns current time to fields based on conditions
        if self.start_job and self.start_time is None:
            self.start_time = timezone.now()
        elif self.completed and self.end_time is None:
            self.end_time = timezone.now()
        elif not self.completed and self.end_time is not None:
            self.end_time = None
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return self.ticket_number
    
    def get_absolute_url(self):
        return reverse("ticket_app:ticket_detail", kwargs={"pk": self.ticket_number})
    

# class PartsUsed(models.Model):
#     part = models.ForeignKey(Part, null=True, on_delete=models.SET_NULL)
#     ticket = models.ForeignKey(Ticket, null=True, on_delete=models.SET_NULL)

#     account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.part) + str(self.ticket)

    
    