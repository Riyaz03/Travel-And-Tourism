# Generated by Django 3.2.1 on 2021-05-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0008_auto_20210515_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='buses',
            name='date',
            field=models.CharField(default='01/01/2021', max_length=10),
        ),
        migrations.AddField(
            model_name='flights',
            name='date',
            field=models.CharField(default='01/01/2021', max_length=10),
        ),
    ]
