# Generated by Django 4.0 on 2022-02-01 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_measurement_sensor_alter_measurement_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
