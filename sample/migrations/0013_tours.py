# Generated by Django 3.1.7 on 2021-05-17 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0012_auto_20210517_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('touristplces_covered', models.CharField(max_length=500)),
                ('hotel', models.CharField(max_length=150)),
                ('cost', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Tours',
            },
        ),
    ]
