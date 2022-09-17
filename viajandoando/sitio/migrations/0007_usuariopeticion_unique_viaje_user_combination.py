# Generated by Django 4.1 on 2022-09-17 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0006_alter_viaje_pasajeros'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='usuariopeticion',
            constraint=models.UniqueConstraint(fields=('viaje', 'user'), name='unique_viaje_user_combination'),
        ),
    ]
