# Generated by Django 4.2.2 on 2023-06-14 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0005_auto_20210610_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='Nombre de estudiante'),
        ),
    ]