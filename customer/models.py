from django.db import models

from phone_field import PhoneField

from accounts.models import AccountCompany

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = PhoneField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    note = models.TextField()
    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.fname + ' ' + self.lname + ' - ' + str(self.company)

class Jobsite(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.PositiveIntegerField()
    contact_name = models.CharField(max_length=100)
    contact_phone = PhoneField()
    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.address1 +' '+ self.address2 +' '+ self.city