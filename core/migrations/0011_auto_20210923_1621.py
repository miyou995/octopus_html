# Generated by Django 3.2.6 on 2021-09-23 15:21

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_service_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='sous catégorie')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Petit text')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Déscription du produit')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='images/categories')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Catégorie'},
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.category', verbose_name='DAS categorie'),
        ),
        migrations.DeleteModel(
            name='SubCategory',
        ),
    ]
