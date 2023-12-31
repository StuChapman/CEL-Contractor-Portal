# Generated by Django 4.2.3 on 2023-07-26 13:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id_no', models.AutoField(primary_key=True, serialize=False)),
                ('orderNumber', models.DecimalField(decimal_places=0, max_digits=10)),
                ('uploadFile', models.FileField(upload_to='media/uploadedfiles/')),
                ('dateUploaded', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'UploadFile',
            },
        ),
    ]
