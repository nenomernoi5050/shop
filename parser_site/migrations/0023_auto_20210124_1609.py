# Generated by Django 3.0.6 on 2021-01-24 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0022_auto_20210124_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardproduct',
            name='url',
            field=models.URLField(null=True, unique=True, verbose_name='Ссылка на оригинал'),
        ),
    ]