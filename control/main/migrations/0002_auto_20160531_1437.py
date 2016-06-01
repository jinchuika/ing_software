# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 14:37
from __future__ import unicode_literals

import datetime
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='fecha_fin',
            field=models.DateField(blank=True, default=datetime.date(2016, 11, 27), null=True),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='fecha_inicio',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='garantia',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=7),
        ),
        migrations.AlterField(
            model_name='tecnico',
            name='salario',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tipoincidencia',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
