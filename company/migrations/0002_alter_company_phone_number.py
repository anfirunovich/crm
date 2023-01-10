# Generated by Django 3.2.7 on 2022-12-27 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.RegexValidator(regex='^\\+375 \\((29|44|33)\\) [0-9]{3}-[0-9]{2}-[0-9]{2}$')], verbose_name='Phone number'),
        ),
    ]
