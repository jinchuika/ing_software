# -*- coding: utf-8 -*-
from django.db import models
from datetime import timedelta, date, time
from decimal import Decimal

class Tecnico(models.Model):
	"""Tabla de empleados"""
	nombre = models.CharField(max_length=100)
	apellido =  models.CharField(max_length=100)
	salario = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return str(self.nombre) + " " + str(self.apellido)

class Cliente(models.Model):
	"""Tabla de clientes"""
	nit = models.CharField(max_length=10, unique=True)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	direccion = models.CharField(max_length=200, blank=True, null=True)
	telefono = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return str(self.nombre) + " " + str(self.apellido)

class TipoEquipo(models.Model):
	"""Tabla para tipos de equipo manejados"""
	descripcion = models.CharField(max_length=50)

	def __str__(self):
		return str(self.descripcion)

class Equipo(models.Model):
	"""Informacion sobre los equipos"""
	cliente = models.ForeignKey('Cliente', on_delete=models.PROTECT)
	tipo_equipo = models.ForeignKey('TipoEquipo', on_delete=models.PROTECT)

	def ver_garantia(self):
		garantia = Garantia.objects.filter(equipo=self).first()
		if garantia:
			return garantia
		else:
			return False

	def generar_codigo(self):
		return str(self.cliente.id)+"-"+str(self.tipo_equipo.id)+"-"+str(self.id)

	def __str__(self):
		return str(self.tipo_equipo) + " de " + str(self.cliente)

class Garantia(models.Model):
	"""Control de las garantías de equipo"""
	equipo = models.ForeignKey('Equipo', on_delete=models.PROTECT)
	fecha_inicio = models.DateField(default=date.today)
	fecha_fin = models.DateField(null=True, blank=True, default=date.today()+timedelta(days=180))
	precio = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.00'))

	def is_valid(self):
		if self.fecha_fin:
			return self.fecha_inicio <= date.today() <= self.fecha_fin
		return self.fecha_inicio <= date.today()

	def ver_vigencia(self):
		if self.is_valid():
			return "vigente"
		else:
			return "vencida"

	def __str__(self):
		return "Garantía del " + str(self.equipo)
		

class TipoIncidencia(models.Model):
	"""Tipos de incidencia que maneja el negocio"""
	descripcion = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=7, decimal_places=2)

	def __str__(self):
		return str(self.descripcion)

class Incidencia(models.Model):
	"""Reporte de daños para una garantía"""
	tipo_incidencia = models.ForeignKey('TipoIncidencia', on_delete=models.PROTECT)
	garantia = models.ForeignKey('Garantia', on_delete=models.PROTECT)
	responsable = models.ForeignKey('Tecnico', default=1, on_delete=models.PROTECT)
	fecha_reporte = models.DateField()
	fecha_solucion = models.DateField(null=True, blank=True)

	def is_solved(self):
		if self.fecha_solucion:
			return date.today() >= self.fecha_solucion
		else:
			return False

	def __str__(self):
		return str(self.tipo_incidencia) + " de la " + str(self.garantia)