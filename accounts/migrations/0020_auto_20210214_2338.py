# Generated by Django 3.1.5 on 2021-02-14 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20210213_2325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='accountuser',
            options={'ordering': ['-account']},
        ),
        migrations.AddField(
            model_name='accountcompany',
            name='membership',
            field=models.CharField(choices=[('Basic', 'Basic'), ('Enterprise', 'Enterprise'), ('Pro', 'Pro')], default='Basic', max_length=254),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Tech', 'Tech')], default='Tech', max_length=20, null=True),
        ),
    ]
