# Generated by Django 3.0.5 on 2020-04-20 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_newcar_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcar',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
