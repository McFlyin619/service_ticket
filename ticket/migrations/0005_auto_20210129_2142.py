# Generated by Django 3.1.5 on 2021-01-29 21:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_ticket_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='schedule',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
