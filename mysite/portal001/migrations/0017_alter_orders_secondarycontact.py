# Generated by Django 4.2.3 on 2023-07-16 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal001', '0016_alter_orders_contractor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='secondaryContact',
            field=models.EmailField(max_length=254),
        ),
    ]