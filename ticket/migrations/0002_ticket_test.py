# Generated by Django 3.1.5 on 2021-01-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='test',
            field=models.CharField(default=True, max_length=999),
            preserve_default=False,
        ),
    ]
