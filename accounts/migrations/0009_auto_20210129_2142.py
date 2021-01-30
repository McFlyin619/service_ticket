# Generated by Django 3.1.5 on 2021-01-29 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20210124_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='company',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tech', 'Tech')], default='Tech', max_length=20, null=True),
        ),
    ]
