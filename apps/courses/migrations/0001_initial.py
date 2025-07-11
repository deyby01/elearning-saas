# Generated by Django 5.2.3 on 2025-06-26 23:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo del Curso')),
                ('description', models.TextField(verbose_name='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Ultima Actualización')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses_taught', to=settings.AUTH_USER_MODEL, verbose_name='Instructor')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='tenants.tenant', verbose_name='Escuela')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
                'ordering': ['-created_at'],
            },
        ),
    ]
