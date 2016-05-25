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