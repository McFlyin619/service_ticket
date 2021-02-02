from django.db import models
from django.contrib.auth.models import User


# Create your models here.
ROLES = {
    ('Admin','Admin'),
    ('Tech','Tech'),
    ('Customer','Customer')
}

class AccountCompany(models.Model):
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class AccountUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)
    company = models.CharField(max_length=100, blank=True)
    role = models.CharField(choices=ROLES, max_length=20, null=True, default='Tech')
    

    def __str__(self):
        return str(self.user.username)

    



