# Generated by Django 3.1.7 on 2021-03-19 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_auto_20210318_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='active',
        ),
        migrations.AddField(
            model_name='game',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
