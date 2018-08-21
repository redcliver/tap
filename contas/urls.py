from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.contas),
    url(r'^nova_conta/$', views.nova_conta),
    url(r'^editar_conta/$', views.editar_conta),
    url(r'^editar_conta1$', views.editar_conta1),
    url(r'^pagar/$', views.pagar),
    ]
