# Generated by Django 4.0 on 2022-03-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='priority',
            field=models.IntegerField(choices=[(0, 'LOW'), (1, 'NORMAL'), (2, 'HIGH'), (3, 'FIRST PRIORITY')], default=3),
        ),
    ]
