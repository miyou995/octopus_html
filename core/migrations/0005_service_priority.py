# Generated by Django 3.2.6 on 2021-09-23 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210920_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='priority',
            field=models.IntegerField(default=1, verbose_name='ordre / priorité'),
            preserve_default=False,
        ),
    ]
