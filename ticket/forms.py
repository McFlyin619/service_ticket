from django import forms
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
        fields = ('ticket_number','t_customer','t_jobsite','assigned','stop','department','t_type','scope','repair_notes','additional_work','schedule','start_job','completed',)
        

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

        