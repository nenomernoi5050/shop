# Generated by Django 3.0.6 on 2021-01-21 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0011_auto_20210121_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardproduct',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='parser_site.CardFoto', verbose_name='Изображения'),
        ),
    ]