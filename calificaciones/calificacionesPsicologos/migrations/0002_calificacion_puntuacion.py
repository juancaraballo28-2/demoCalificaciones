# Generated by Django 4.0.3 on 2022-03-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calificacionesPsicologos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calificacion',
            name='puntuacion',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
