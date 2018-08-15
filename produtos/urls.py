from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.produtos),
    url(r'^base/$', views.base),
    url(r'^nova_base/$', views.nova_base),
    url(r'^editar_base/$', views.editar_base),
    url(r'^editar_base1/$', views.editar_base1),
    url(r'^add/$', views.add),
    url(r'^novo_add/$', views.novo_add),
    url(r'^editar_add/$', views.editar_add),
    url(r'^editar_add1/$', views.editar_add1),
    url(r'^novo/$', views.novo),
    url(r'^editar/$', views.editar),
    url(r'^editar1/$', views.editar1),
    
    ]
