# Generated by Django 3.1.6 on 2023-03-27 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20230321_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='iamge',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]