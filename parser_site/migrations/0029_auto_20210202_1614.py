# Generated by Django 3.0.6 on 2021-02-02 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_site', '0028_auto_20210201_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardproduct',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='cardproduct',
            name='subcategory',
            field=models.ManyToManyField(null=True, to='parser_site.Subcategory'),
        ),
    ]