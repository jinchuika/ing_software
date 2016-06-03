from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from main.models import *
from main.forms import *
from django.views.generic import UpdateView
from django.http import Http404


def index(request):
	incidencia_list = Incidencia.objects.filter(
		Q(Q(fecha_solucion__gt=date.today()) | Q(fecha_solucion=None))
	).order_by('fecha_reporte')
	return render(request, 'main/index.html', {'incidencia_list': incidencia_list})

def cliente_index(request):
	cliente_list = Cliente.objects.all().order_by('nombre')
	return render(request, 'c/index.html', {'cliente_list': cliente_list})

def cliente_detail(request, id_cliente):
	cliente = Cliente.objects.filter(id=id_cliente).first()
	equipo_data = Equipo.objects.filter(cliente=cliente)
	equipo_list = []
	for equipo in equipo_data:
		garantia = Garantia.objects.filter(equipo=equipo).first()
		if garantia:
			garantia = garantia
			#garantia = garantia.is_valid()
		else:
			garantia = 'Sin garantía'
		equipo_list.append({'descripcion':equipo,'garantia': garantia})
	context = {
		'cliente': cliente, 'equipo_list': equipo_list
	}
	return render(request, 'c/detail.html', context)

def cliente_edit(request, id_cliente):
	cliente = Cliente.objects.filter(id=id_cliente).first()

	if request.method=='POST':
		cliente_form = ClienteModelForm(request.POST, instance = cliente)
		if cliente_form.is_valid():
			cliente = cliente_form.save(commit=False)
			cliente.save()
			return redirect('cliente_detail', id_cliente=cliente.id)
	else:
		data = {'id': cliente.id, 'nit': cliente.nit, 'nombre':cliente.nombre, 'apellido': cliente.apellido, 'direccion': cliente.direccion, 'telefono': cliente.telefono}
		cliente_form = ClienteModelForm(initial=data)
	return render(request, 'c/add.html', {'cliente_form': cliente_form})

def cliente_add(request):
	if request.method=='POST':
		cliente_form = ClienteModelForm(request.POST)
		if cliente_form.is_valid():
			cliente = cliente_form.save(commit=False)
			cliente.save()
			return redirect('cliente_detail', id_cliente=cliente.id)
	else:
		cliente_form = ClienteModelForm()
	return render(request, 'c/add.html', {'cliente_form': cliente_form})

def cliente_delete(request, id_cliente):
	Cliente.objects.filter(id=id_cliente).delete()
	return redirect('cliente_index')

def tipo_equipo_index(request):
	if request.method=='POST':
		tipo_equipo_form = TipoEquipoModelForm(request.POST)
		if tipo_equipo_form.is_valid():
			tipo_equipo = tipo_equipo_form.save(commit=False)
			tipo_equipo.save()
			return redirect('tipo_equipo_index')
	else:
		tipo_equipo_form = TipoEquipoModelForm()

	tipo_equipo_list = TipoEquipo.objects.all()
	return render(request, 'e/tipo.html', {'tipo_equipo_list':tipo_equipo_list,'tipo_equipo_form': tipo_equipo_form})

def equipo_index(request):
	equipo_list = Equipo.objects.all()
	return render(request, 'e/index.html', {'equipo_list':equipo_list})

def equipo_add(request, id_cliente=None):
	if request.method=='POST':
		equipo_form = EquipoModelForm(request.POST)
		if equipo_form.is_valid():
			equipo = equipo_form.save(commit=False)
			equipo.save()
			return redirect('garantia_add_equipo', id_equipo=equipo.id)
	else:
		if id_cliente:
			cliente = Cliente.objects.filter(id=id_cliente).first()
			equipo_form = EquipoModelForm(initial={'cliente': cliente})
		else:
			equipo_form = EquipoModelForm()
	return render(request, 'e/add.html', {'equipo_form': equipo_form})

def equipo_detail(request, id_equipo):
	equipo = get_object_or_404(Equipo, id=id_equipo)
	return render(request, 'e/detail.html', {'equipo':equipo})

def garantia_index(request):
	garantia_list = Garantia.objects.all()
	return render(request, 'g/index.html', {'garantia_list': garantia_list})

def garantia_add(request, id_equipo=None, id_garantia=None):
	equipo = Equipo.objects.filter(id=id_equipo).first()
	garantia = Garantia.objects.filter(id=id_garantia).first()
	if request.method=='POST':
		if garantia:
			garantia_form = GarantiaModelForm(request.POST, instance=garantia, initial={'fecha_inicio':garantia.fecha_inicio})
		else:
			garantia_form = GarantiaModelForm(request.POST)
		if garantia_form.is_valid():
			garantia = garantia_form.save(commit=False)
			garantia.save()
			return redirect('garantia_detail', id_garantia=garantia.id)
	else:
		if equipo and garantia:
			garantia_form = GarantiaModelForm(initial={'equipo':equipo, 'fecha_inicio': garantia.fecha_inicio, 'fecha_fin': garantia.fecha_fin})
		elif equipo:
			garantia_form = GarantiaModelForm(initial={'equipo':equipo})
		elif garantia:
			garantia_form = GarantiaModelForm(initial={'equipo':garantia.equipo, 'fecha_inicio': garantia.fecha_inicio, 'fecha_fin': garantia.fecha_fin})
		else:
			garantia_form = GarantiaModelForm()
	return render(request, 'g/add.html', {'garantia_form': garantia_form})

def garantia_detail(request, id_garantia, id_incidencia=None):
	garantia = get_object_or_404(Garantia, id=id_garantia)
	incidencia_list = Incidencia.objects.filter(garantia=garantia).order_by('fecha_reporte')
	incidencia = Incidencia.objects.filter(id=id_incidencia).first()

	if request.method=='POST':
		if incidencia:
			incidencia_form = IncidenciaModelForm(request.POST, instance=incidencia)
		else:
			incidencia_form = IncidenciaModelForm(request.POST)
		if incidencia_form.is_valid():
			incidencia = incidencia_form.save(commit=False)
			incidencia.save()
			return redirect('garantia_detail', id_garantia=id_garantia)
	else:
		if incidencia:
			incidencia_form = IncidenciaModelForm(instance=incidencia)
		else:
			incidencia_form = IncidenciaModelForm(initial={'garantia':garantia, 'fecha_reporte': date.today()})
	
	context = {
		'garantia': garantia,
		'incidencia_list': incidencia_list,
		'incidencia_form': incidencia_form
	}
	if incidencia:
		context['incidencia'] = incidencia
	return render(request, 'g/detail.html', context)

def informe_tipo(request):
	incidencia_list = []
	total = Incidencia.objects.count()
	for tipo in Incidencia.objects.values('tipo_incidencia').distinct():
		incidencia_desc = TipoIncidencia.objects.get(id=tipo['tipo_incidencia'])
		cuenta = Incidencia.objects.filter(tipo_incidencia=tipo['tipo_incidencia']).count()
		porcentaje = (cuenta/total)*100
		incidencia_list.append({
			'descripcion': incidencia_desc,
			'cantidad': cuenta,
			'porcentaje': porcentaje
		})
	incidencia_list = sorted(incidencia_list, reverse=True, key=lambda incidencia: incidencia['cantidad'])
	for index, incidencia in enumerate(incidencia_list):
		suma = 0
		suma_p = 0
		for x in range(0,index+1):
			suma += incidencia_list[x]['porcentaje']
		incidencia['index'] = index
		incidencia['suma'] = suma
		incidencia['resta'] = 100 - suma

	return render(request, 'z/index.html', {'incidencia_list': incidencia_list})
