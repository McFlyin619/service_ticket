# Generated by Django 3.1.5 on 2021-02-13 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210212_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Admin', 'Admin')], default='Tech', max_length=20, null=True),
        ),
    ]