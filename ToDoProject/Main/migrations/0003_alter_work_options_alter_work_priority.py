# Generated by Django 4.0 on 2022-03-17 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_work_priority'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['-date_created', 'priority']},
        ),
        migrations.AlterField(
            model_name='work',
            name='priority',
            field=models.IntegerField(choices=[(0, 'LOW'), (1, 'NORMAL'), (2, 'HIGH'), (3, 'FIRST PRIORITY')], default=2),
        ),
    ]
