# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centro', '0002_cursos_equipoeducativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='EquipoEducativo',
            field=models.ManyToManyField(blank=True, null=True, to='centro.Profesores', verbose_name='Equipo Educativo'),
        ),
    ]