# Generated by Django 3.0.6 on 2021-02-12 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_pagehit_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagehit',
            name='url',
        ),
    ]
