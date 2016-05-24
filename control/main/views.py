from django.shortcuts import render
from main.models import *

def index(request):
	return render(request, 'main/index.html')

def cliente_index(request):
	cliente_list = Cliente.objects.all().order_by('nombre')
	return render(request, 'c/index.html', {'cliente_list': cliente_list})

def cliente_detail(request, id_cliente):
	cliente = Cliente.objects.get(id=id_cliente)
	return render(request, 'c/detail.html', {'cliente': cliente})
