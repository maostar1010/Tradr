# Generated by Django 3.1.6 on 2023-03-21 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20230321_1743'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='icondition',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='tag',
        ),
    ]