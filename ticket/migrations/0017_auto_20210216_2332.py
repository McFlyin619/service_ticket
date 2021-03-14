# Generated by Django 3.1.5 on 2021-02-16 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20210216_2332'),
        ('ticket', '0016_remove_ticket_parts_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='assigned',
        ),
        migrations.AddField(
            model_name='ticket',
            name='assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.accountuser'),
        ),
    ]