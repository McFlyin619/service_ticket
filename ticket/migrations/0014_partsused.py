# Generated by Django 3.1.5 on 2021-02-06 21:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20210206_0039'),
        ('part', '0003_auto_20210206_0039'),
        ('ticket', '0013_remove_ticket_parts_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartsUsed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.accountcompany')),
                ('part', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='part.part')),
                ('ticket', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.ticket')),
            ],
        ),
    ]
