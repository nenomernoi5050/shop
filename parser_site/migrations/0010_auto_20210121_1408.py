# Generated by Django 3.0.6 on 2021-01-21 11:08

from django.db import migrations, models
import django.db.models.deletion
import parser_site.models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0009_auto_20210121_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardfoto',
            name='product',
            field=models.CharField(default=1, max_length=100, verbose_name=parser_site.models.CardProduct),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cardproduct',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parser_site.CardFoto', verbose_name='Изображения'),
        ),
    ]
