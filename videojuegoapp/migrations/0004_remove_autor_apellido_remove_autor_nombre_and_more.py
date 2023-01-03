# Generated by Django 4.1.3 on 2023-01-03 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('videojuegoapp', '0003_alter_autor_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autor',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='autor',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='autor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
