from django import forms
from django.contrib.auth.models import User
from django.db.models.query import QuerySet

from .models import *


class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = 'ticket_number','t_customer','t_jobsite','assigned','stop','department','t_type','scope','repair_notes','additional_work','schedule','start_job','completed',

     

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["t_customer"].label = "Sold To"
        self.fields["t_jobsite"].label = "Jobsite"
        self.fields["assigned"].label = "Technician"
        self.fields["department"].label = "Dept"
        self.fields["t_type"].label = "Service Type"

class TicketUpdateForm(forms.ModelForm):
    ticket_number = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model = Ticket
        fields = ('ticket_number','t_customer','t_jobsite','assigned','stop','department','t_type','scope','repair_notes','additional_work','schedule','start_time','end_time','start_job','completed',)
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["t_customer"].label = "Sold To"
        self.fields["t_jobsite"].label = "Jobsite"
        self.fields["assigned"].label = "Technician"
        self.fields["department"].label = "Dept"
        self.fields["t_type"].label = "Service Type"

class TechTicketUpdateForm(forms.ModelForm):
    ticket_number = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    
    class Meta:
        model = Ticket
        fields = ('ticket_number','start_job','completed','repair_notes','additional_work')      

# class PartsUsedForm(forms.ModelForm):
#     class Meta:
#         model = PartsUsed 
#         fields = ('part',)     
