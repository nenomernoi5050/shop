# Generated by Django 3.0.6 on 2021-01-21 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0004_cardfoto_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardfoto',
            name='product',
        ),
    ]
