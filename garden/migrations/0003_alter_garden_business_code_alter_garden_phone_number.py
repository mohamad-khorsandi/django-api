# Generated by Django 4.2 on 2023-05-29 08:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0002_alter_garden_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='garden',
            name='business_code',
            field=models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(12)]),
        ),
        migrations.AlterField(
            model_name='garden',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.MinLengthValidator(11)]),
        ),
    ]
