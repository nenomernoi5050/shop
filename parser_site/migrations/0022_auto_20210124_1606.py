# Generated by Django 3.0.6 on 2021-01-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0021_auto_20210124_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardproduct',
            name='desc_one',
            field=models.TextField(null=True, verbose_name='Описание часть 1'),
        ),
        migrations.AlterField(
            model_name='cardproduct',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена'),
        ),
    ]
