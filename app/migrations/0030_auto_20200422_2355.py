# Generated by Django 3.0.5 on 2020-04-22 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_auto_20200422_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='year',
            field=models.DateTimeField(),
        ),
    ]