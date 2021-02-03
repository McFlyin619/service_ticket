# Generated by Django 3.1.5 on 2021-02-02 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20210130_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Customer', 'Customer'), ('Admin', 'Admin'), ('Tech', 'Tech')], default='Tech', max_length=20, null=True),
        ),
    ]
