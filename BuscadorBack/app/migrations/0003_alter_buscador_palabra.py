# Generated by Django 4.0 on 2021-12-08 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_buscador_primer_busqueda_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buscador',
            name='palabra',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
