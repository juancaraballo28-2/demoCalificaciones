# Generated by Django 4.0.3 on 2022-03-16 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Psicologo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=200)),
                ('psicologo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calificacionesPsicologos.psicologo')),
            ],
        ),
    ]
