from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^c$', views.cliente_index, name='cliente_index'),
	url(r'^c/(?P<id_cliente>[0-9]+)/$', views.cliente_detail, name='cliente_detail'),
	url(r'^c/(?P<id_cliente>[0-9]+)/edit$', views.cliente_edit, name='cliente_edit'),
	url(r'^c/(?P<id_cliente>[0-9]+)/delete$', views.cliente_delete, name='cliente_delete'),
	url(r'^c/add$', views.cliente_add, name='cliente_add'),
]