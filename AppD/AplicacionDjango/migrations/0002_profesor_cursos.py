# Generated by Django 4.2 on 2023-04-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicacionDjango', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesor',
            name='cursos',
            field=models.ManyToManyField(to='AplicacionDjango.curso'),
        ),
    ]