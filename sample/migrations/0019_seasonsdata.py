# Generated by Django 3.2.1 on 2021-05-19 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0018_alter_buses_ac_sleeper'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonsData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=100)),
                ('population', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'SeasonalData',
            },
        ),
    ]
