# Generated by Django 3.1.5 on 2021-02-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20210209_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tech', 'Tech')], default='Tech', max_length=20, null=True),
        ),
    ]
