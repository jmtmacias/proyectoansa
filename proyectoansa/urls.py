from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyectoansa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'usuarios.views.home', name='home'),
	url(r'^login/','usuarios.views.login_page',name='login'),
	url(r'^logout/$','usuarios.views.cerrar_sesion',name='logout'),
	url(r'^definir/banco/$','usuarios.views.banco',name='banco'),
	url(r'^definir/usuario/lista/$','usuarios.views.listar_usuarios',name='listar_usuarios'),
	url(r'^definir/usuario/nuevo/$','usuarios.views.usuario_nuevo',name='usuario_nuevo'),
)
