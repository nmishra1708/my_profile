# Generated by Django 3.1.4 on 2020-12-11 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_auto_20201211_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='owner',
        ),
    ]
