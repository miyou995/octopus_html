# Generated by Django 3.2.6 on 2021-10-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='linkedin',
            field=models.URLField(blank=True, max_length=300, null=True, verbose_name='Lien page LinkedIn'),
        ),
    ]
