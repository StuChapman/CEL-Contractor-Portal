# Generated by Django 4.2.3 on 2023-07-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal001', '0014_alter_orders_primarycontact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractors',
            name='secondaryContact',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='username', to='portal001.contractors'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='secondaryContact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email', to='portal001.contractors', to_field='secondaryContact'),
        ),
    ]