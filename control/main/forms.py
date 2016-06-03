from django import forms
from django.forms import ModelForm
from main.models import *
import datetime

class ClienteModelForm(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'

class TipoEquipoModelForm(ModelForm):
	"""Formulario para el modelo de tipo de equipo"""
	class Meta:
		model = TipoEquipo
		fields = '__all__'

class EquipoModelForm(ModelForm):
	"""Formulario para crear nuevo equipo"""
	class Meta:
		model = Equipo
		fields = '__all__'

class GarantiaModelForm(ModelForm):
	class Meta:
		model = Garantia
		fields = '__all__'

	def clean(self):
		fecha_inicio = self.cleaned_data.get("fecha_inicio")
		fecha_fin = self.cleaned_data.get("fecha_fin")
		if fecha_fin:
			if fecha_fin < fecha_inicio:
				msg = u"Fecha de fin debe ser mayor a la de inicio."
				self._errors["fecha_fin"] = self.error_class([msg])
			if date.today() > fecha_fin:
				msg = u"Fecha de fin debe ser después de hoy"
				self._errors["fecha_fin"] = self.error_class([msg])

class IncidenciaModelForm(ModelForm):
	class Meta:
		model = Incidencia
		fields = '__all__'
		widgets = {'garantia': forms.HiddenInput()}

	def clean(self):
		fecha_reporte = self.cleaned_data.get("fecha_reporte")
		fecha_solucion = self.cleaned_data.get("fecha_solucion")
		if fecha_solucion:
			if fecha_solucion < fecha_reporte:
				msg = u"Fecha de solución debe ser mayor a la de reporte."
				self._errors["fecha_solucion"] = self.error_class([msg])
			if date.today() < fecha_solucion:
				msg = u"Fecha de solución no debe ser mayor a hoy"
				self._errors["fecha_solucion"] = self.error_class([msg])