# Generated by Django 3.1.5 on 2021-02-02 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210202_2216'),
        ('ticket', '0010_auto_20210129_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.serviceprovided'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='t_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='t_jobsite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.jobsite'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='t_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ticket.tickettype'),
        ),
    ]