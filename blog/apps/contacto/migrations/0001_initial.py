# Generated by Django 4.2.3 on 2023-07-25 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('asunto', models.CharField(max_length=50)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]