from django import forms
from .models import *
from ticket.models import Ticket



class CustomerCreateForm(forms.ModelForm):
    
    
    class Meta:
        model = Customer
        fields = ('fname','lname','email','phone_number','company','note',)
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fname"].label = "First Name"
        self.fields["lname"].label = "Last Name"