# Generated by Django 3.1.5 on 2021-01-24 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_ticket_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='test',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='additional_work',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_number',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
