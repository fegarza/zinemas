from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio' ),
    url(r'^resultados/$', views.busqueda, name='busqueda'),
    url(r'^login/$', views.entrar, name='login'),
    url(r'^terminos/', views.terminos, name='terminos'),
    url(r'^reproductor/(?P<pk>[0-9]+)/$', views.reproductor, name='reproductor'),
    url(r'^perfil/(?P<pk>[0-9]+)/$', views.perfil, name='perfil'),
    url(r'^logout/$', auth_views.logout, {'next_page' : '/'}, name='logout'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^actualizar/$', views.actualizar_perfil, name='actualizar'),
    url(r'sugerencias/$',views.sugerencias, name='sugerencias'),
    url(r'categorias/$', views.categorias, name='categoria'),
    url(r'agr_fav/$', views.agr_fav, name='agr_fav'),
    url(r'agr_val/$', views.agr_valoracion, name='agr_val'),
    url(r'categoria/$', views.categoriam, name='cate'),
]
