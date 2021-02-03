from django import forms
from .models import *

class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('fname','lname','email','phone_number','company','note',)
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["fname"].label = "First Name"
        self.fields["lname"].label = "Last Name"

class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address1"].label = "Address"
        self.fields["address2"].label = "Address 2"
    
class JobsiteCreateForm(forms.ModelForm):
    class Meta:
        model = Jobsite
        exclude = ('account',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address1"].label = "Address"
        self.fields["address2"].label = "Address 2"