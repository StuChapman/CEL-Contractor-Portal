# Generated by Django 4.2.3 on 2023-07-20 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contractors',
            fields=[
                ('contractor', models.CharField(max_length=254, primary_key=True, serialize=False)),
                ('secondaryContact', models.EmailField(max_length=254, unique=True)),
                ('services', models.CharField(blank=True, max_length=9999, null=True)),
            ],
            options={
                'verbose_name_plural': 'Contractors',
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('orderNumber', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('readUnread', models.DecimalField(decimal_places=0, default=0, max_digits=1)),
            ],
            options={
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('orderNumber', models.DecimalField(decimal_places=0, max_digits=10, primary_key=True, serialize=False)),
                ('orderDescription', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('appointmentDate', models.DateTimeField(blank=True, null=True)),
                ('secondaryContact', models.EmailField(max_length=254)),
                ('notes', models.CharField(blank=True, max_length=9999, null=True)),
                ('dateLastUpdate', models.DateTimeField(default=django.utils.timezone.now)),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='portal001.contractors')),
                ('primaryContact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
    ]
