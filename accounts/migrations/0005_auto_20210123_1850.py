# Generated by Django 3.1.5 on 2021-01-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210121_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tech', 'Tech')], default='Tech', max_length=20, null=True),
        ),
    ]