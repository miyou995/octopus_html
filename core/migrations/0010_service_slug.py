# Generated by Django 3.2.6 on 2021-09-23 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20210923_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slug',
            field=models.SlugField(default='hello'),
            preserve_default=False,
        ),
    ]
