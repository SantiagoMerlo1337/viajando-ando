# Generated by Django 4.1 on 2022-09-06 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0011_alter_viaje_datetime_alter_viaje_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='fecha',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='viaje',
            name='hora',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]