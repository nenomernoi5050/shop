# Generated by Django 3.0.6 on 2021-02-05 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0033_remove_cardproduct_desc_two'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardproduct',
            name='images',
        ),
    ]
