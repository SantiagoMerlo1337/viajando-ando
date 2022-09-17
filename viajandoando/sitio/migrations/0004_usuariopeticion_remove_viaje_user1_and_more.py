# Generated by Django 4.1 on 2022-09-16 20:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0003_alter_viaje_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioPeticion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estaAceptado', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='viaje',
            name='user2',
        ),
        migrations.AddField(
            model_name='viaje',
            name='ocupados',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='viaje',
            name='pasajeros',
            field=models.ManyToManyField(default=None, null=True, through='sitio.UsuarioPeticion', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usuariopeticion',
            name='viaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sitio.viaje'),
        ),
    ]
