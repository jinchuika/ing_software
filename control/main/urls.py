from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^c$', views.cliente_index, name='cliente_index'),
	url(r'^c/(?P<id_cliente>[0-9]+)/$', views.cliente_detail, name='cliente_detail'),
	url(r'^c/(?P<id_cliente>[0-9]+)/edit$', views.cliente_edit, name='cliente_edit'),
	url(r'^c/(?P<id_cliente>[0-9]+)/delete$', views.cliente_delete, name='cliente_delete'),
	url(r'^c/add$', views.cliente_add, name='cliente_add'),

	url(r'^e$', views.equipo_index, name='equipo_index'),
	url(r'^e/tipo$', views.tipo_equipo_index, name='tipo_equipo_index'),
	url(r'^e/add$', views.equipo_add, name='equipo_add'),
	url(r'^e/add/(?P<id_cliente>[0-9]+)/$', views.equipo_add, name='equipo_add_cliente'),
	url(r'^e/(?P<id_equipo>[0-9]+)/$', views.equipo_detail, name='equipo_detail'),

	url(r'^g$', views.garantia_index, name='garantia_index'),
	url(r'^g/add$', views.garantia_add, name='garantia_add'),
	url(r'^g/add/(?P<id_equipo>[0-9]+)/$', views.garantia_add, name='garantia_add_equipo'),
	url(r'^g/add/(?P<id_equipo>[0-9]+)/(?P<id_garantia>[0-9]+)/$', views.garantia_add, name='garantia_add_edit'),
	url(r'^g/(?P<id_garantia>[0-9]+)/$', views.garantia_detail, name='garantia_detail'),
	url(r'^g/(?P<id_garantia>[0-9]+)/(?P<id_incidencia>[0-9]+)$', views.garantia_detail, name='garantia_detail_incidencia'),

	url(r'^z$', views.informe_tipo, name='informe_tipo'),
]