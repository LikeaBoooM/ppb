# Generated by Django 3.0.5 on 2020-04-22 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20200422_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='year',
            field=models.CharField(default=None, max_length=32),
        ),
    ]
