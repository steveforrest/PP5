# Generated by Django 3.2 on 2022-06-06 12:07

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_auto_20220527_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]