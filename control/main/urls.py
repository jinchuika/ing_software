from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^c$', views.cliente_index, name='cliente_index'),
	url(r'^c/(?P<id_cliente>[0-9]+)/$', views.cliente_detail, name='cliente_detail'),
]