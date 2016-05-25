# -*- coding: utf-8 -*-
from django.db import models
from datetime import timedelta, date, time

class Tecnico(models.Model):
	"""Tabla de empleados"""
	nombre = models.CharField(max_length=100)
	apellido =  models.CharField(max_length=100)
	salario = models.DecimalField(max_digits=5, decimal_places=2)

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
	cliente = models.ForeignKey('Cliente')
	tipo_equipo = models.ForeignKey('TipoEquipo')

	def __str__(self):
		return str(self.tipo_equipo) + " de " + str(self.cliente)

class Garantia(models.Model):
	"""Control de las garantías de equipo"""
	equipo = models.ForeignKey('Equipo')
	fecha_inicio = models.DateField(default=date.today)
	fecha_fin = models.DateField(null=True, blank=True, default=date.today()+timedelta(days=180))
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	def isValid(self):
		if self.fecha_fin:
			return self.fecha_inicio <= date.today() <= self.fecha_fin
		return self.fecha_inicio <= date.today()

	def __str__(self):
		return "garantía del " + str(self.equipo) + str(self.isValid())
		

class TipoIncidencia(models.Model):
	"""Tipos de incidencia que maneja el negocio"""
	descripcion = models.CharField(max_length=50)
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.descripcion)

class Incidencia(models.Model):
	"""Reporte de daños para una garantía"""
	tipo_incidencia = models.ForeignKey('TipoIncidencia')
	garantia = models.ForeignKey('Garantia')
	responsable = models.ForeignKey('Tecnico', default=1)
	fecha_reporte = models.DateField()
	fecha_solucion = models.DateField(null=True, blank=True)

	def __str__(self):
		return str(self.tipo_incidencia) + " de la " + str(self.garantia)

class Factura(models.Model):
	"""Facturas para las ventas"""
	nit_cliente = models.ForeignKey('Cliente')
	fecha = models.DateField()

	def __str__(self):
		return str(self.nit_cliente)

class DetalleFactura(models.Model):
	"""Detalle para cada item de la factura"""
	factura = models.ForeignKey('Factura', default=1)
	incidencia = models.ForeignKey('Incidencia', null=True, blank=True)
	garantia = models.ForeignKey('Garantia', null=True, blank=True)
	precio = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return str(self.incidencia) + " en " + str(self.garantia)