# Generated by Django 3.0.6 on 2021-01-21 10:22

from django.db import migrations, models
import parser_site.models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0005_remove_cardfoto_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardfoto',
            name='product',
            field=models.CharField(default=1, max_length=100, verbose_name=parser_site.models.CardProduct),
            preserve_default=False,
        ),
    ]
