# Generated by Django 4.0 on 2022-10-18 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosAccidentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_text', models.CharField(max_length=200)),
                ('calle_text', models.CharField(max_length=200)),
                ('autos_numero', models.IntegerField()),
                ('personas_afectadas', models.IntegerField()),
                ('descripcion_text', models.CharField(max_length=200)),
                ('municipio_text', models.CharField(max_length=200)),
                ('departamento_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DatosCoop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_text', models.CharField(max_length=200)),
                ('calle_text', models.CharField(max_length=200)),
                ('autos_numero', models.IntegerField()),
                ('personas_afectadas', models.IntegerField()),
                ('descripcion_text', models.CharField(max_length=200)),
                ('municipio_text', models.CharField(max_length=200)),
                ('departamento_text', models.CharField(max_length=200)),
            ],
        ),
    ]