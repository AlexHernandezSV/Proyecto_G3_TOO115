# Generated by Django 4.1.1 on 2022-10-22 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cobros', '0003_cuota_fecha_fin_cuota_fecha_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuota',
            name='monto',
            field=models.FloatField(null=True),
        ),
    ]