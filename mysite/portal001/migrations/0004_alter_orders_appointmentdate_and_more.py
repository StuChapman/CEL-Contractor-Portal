# Generated by Django 4.2.3 on 2023-07-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal001', '0003_alter_orders_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='appointmentDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='dateLastUpdate',
            field=models.DateTimeField(),
        ),
    ]