# Generated by Django 4.0 on 2022-03-17 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_alter_work_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work',
            options={'ordering': ['-priority', '-date_created']},
        ),
    ]
