from django.db import models
from accounts.models import AccountCompany
# Create your models here.

class Part(models.Model):
    name = models.CharField(max_length=256)
    part_no = models.CharField(max_length=256)
    vendor = models.CharField(max_length=256)
    stock = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

    def __str__(self):
        return self.name