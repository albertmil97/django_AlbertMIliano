# Generated by Django 3.0.7 on 2020-06-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference', '0003_auto_20200613_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=255), max_length=255, unique_for_date='create'),
        ),
    ]
