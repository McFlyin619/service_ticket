# Generated by Django 3.1.5 on 2021-01-24 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20210123_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Tech', 'Tech'), ('Admin', 'Admin')], default='Tech', max_length=20, null=True),
        ),
    ]
