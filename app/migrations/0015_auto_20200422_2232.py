# Generated by Django 3.0.5 on 2020-04-22 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20200422_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='newcar',
            name='year',
            field=models.DateField(blank=True, default=2005, null=True),
        ),
    ]