from django.test import TestCase
from main.models import *
from main.forms import *
from decimal import Decimal
# Create your tests here.

class IncidenciaFormTest(TestCase):
	def test_validate(self):
		data = {
			'tipo_incidencia': 1,
			'responsable': Tecnico.objects.all().first(),
			'fecha_reporte': '2016-05-01',
			'fecha_solucion': '2016-06-03',
		}

		incidencia = Incidencia(data)
		incidencia_form = IncidenciaModelForm(data, instance=incidencia)
		print(incidencia_form.errors)
		self.assertEquals(incidencia_form.is_valid(), True)