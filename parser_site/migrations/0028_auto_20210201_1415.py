# Generated by Django 3.0.6 on 2021-02-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0027_remove_cardproduct_url_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardproduct',
            name='slug',
            field=models.CharField(max_length=150, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='cardproduct',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
    ]
