from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$','aplicacion.views.mostrar'),
	url(r'^ej1/','aplicacion.views.ej1'),
	url(r'^ej2/','aplicacion.views.ej2'),
	url(r'^ej3/','aplicacion.views.ej3'),
	url(r'^ej4/','aplicacion.views.ej4'),
	url(r'^barra/','aplicacion.views.barra'),
]
