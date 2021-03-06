# Generated by Django 3.2.6 on 2021-10-07 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20211007_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='analytics',
            field=models.TextField(blank=True, null=True, verbose_name='Google Analytics'),
        ),
        migrations.AlterField(
            model_name='business',
            name='analytics2',
            field=models.TextField(blank=True, null=True, verbose_name='Analytics 2'),
        ),
        migrations.AlterField(
            model_name='business',
            name='messenger',
            field=models.TextField(blank=True, null=True, verbose_name='Facebook Messenger'),
        ),
        migrations.AlterField(
            model_name='business',
            name='pixel',
            field=models.TextField(blank=True, null=True, verbose_name='Facebook Pixel'),
        ),
    ]
