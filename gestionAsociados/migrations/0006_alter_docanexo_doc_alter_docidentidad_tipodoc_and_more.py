# Generated by Django 4.1.1 on 2022-10-27 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_administrador_aspirante_cajero_jefeoperaciones_and_more'),
        ('gestionAsociados', '0005_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docanexo',
            name='doc',
            field=models.FileField(blank=True, null=True, upload_to='documentos'),
        ),
        migrations.AlterField(
            model_name='docidentidad',
            name='tipoDoc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionAsociados.tipodocidentidad'),
        ),
        migrations.AlterField(
            model_name='peticionadmision',
            name='nombre3',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='vivienda',
            name='tenenciaVivienda',
            field=models.CharField(choices=[('Propia', 'Propia'), ('Alquilada', 'Alquilada'), ('Promesa de venta', 'Promesa de venta'), ('Familiar', 'Familiar')], max_length=30),
        ),
        migrations.CreateModel(
            name='ReciboIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descripcion', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=30)),
                ('aspirante', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.aspirante')),
            ],
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=8)),
                ('tipo', models.CharField(max_length=10)),
                ('saldo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('aspirante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.aspirante')),
            ],
        ),
    ]