# Generated by Django 4.2.3 on 2023-07-10 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal001', '0019_remove_orders_orderclosed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contractors',
            name='id_no',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='id_no',
        ),
    ]
