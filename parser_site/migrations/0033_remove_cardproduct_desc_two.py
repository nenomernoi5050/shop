# Generated by Django 3.0.6 on 2021-02-05 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0032_auto_20210204_1430'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardproduct',
            name='desc_two',
        ),
    ]
