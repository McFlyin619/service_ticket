from django.urls.base import reverse
from accounts.models import AccountCompany
from django.db import models
import datetime
from django.db.models.fields import DateField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=999)
    date = models.DateField(default=datetime.date.today)
    account = models.ForeignKey(AccountCompany, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("upcoming:post_detail", kwargs={"pk": self.pk})
    
    