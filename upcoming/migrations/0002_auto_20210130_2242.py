# Generated by Django 3.1.5 on 2021-01-30 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upcoming', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_one',
            new_name='date',
        ),
    ]
