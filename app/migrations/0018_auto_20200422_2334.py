# Generated by Django 3.0.5 on 2020-04-22 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20200422_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='price',
            field=models.PositiveIntegerField(default=2005),
        ),
    ]
