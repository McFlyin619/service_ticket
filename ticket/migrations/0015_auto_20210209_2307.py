# Generated by Django 3.1.5 on 2021-02-09 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0014_partsused'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='parts_used',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='PartsUsed',
        ),
    ]
