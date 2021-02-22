# Generated by Django 3.1.5 on 2021-02-16 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20210215_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountcompany',
            name='membership',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Pro', 'Pro'), ('Enterprise', 'Enterprise')], default='Basic', max_length=254),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tech', 'Tech')], default='Tech', max_length=20, null=True),
        ),
    ]
