# Generated by Django 3.0.6 on 2021-01-21 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0003_auto_20210121_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardfoto',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='parser_site.CardProduct', verbose_name='Товар'),
        ),
    ]
