# Generated by Django 3.2.7 on 2022-12-25 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_language_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='languages',
            field=models.ManyToManyField(related_name='languages', related_query_name='languages', to='company.Language'),
        ),
    ]
