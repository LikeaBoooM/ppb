# Generated by Django 3.0.5 on 2020-04-22 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20200422_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='year',
            field=models.CharField(default=2010, max_length=32),
        ),
    ]
