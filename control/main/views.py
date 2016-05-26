from django.shortcuts import render, redirect, get_object_or_404
from main.models import *
from main.forms import *
from django.views.generic import UpdateView
from django.http import Http404

def index(request):
	return render(request, 'main/index.html')

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
			garantia = garantia.isValid()
		else:
			garantia = 'Sin garantía'
		equipo_list.append({'descripcion':equipo,'garantia': garantia})
	return render(request, 'c/detail.html', {'cliente': cliente, 'equipo_list': equipo_list})

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