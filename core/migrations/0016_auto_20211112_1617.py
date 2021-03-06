# Generated by Django 3.2.6 on 2021-11-12 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_alter_service_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom complet')),
                ('phone', models.CharField(max_length=25, verbose_name='Téléphone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('subject', models.CharField(blank=True, max_length=50, null=True, verbose_name='Sujet')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Message')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Formulaire de contact',
                'verbose_name_plural': 'Formulaire de contact',
                'ordering': ('id',),
            },
        ),
        migrations.DeleteModel(
            name='ContactForm',
        ),
    ]
