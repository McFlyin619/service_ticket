# Generated by Django 3.1.5 on 2021-02-06 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20210205_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tech', 'Tech')], default='Tech', max_length=20, null=True),
        ),
    ]
