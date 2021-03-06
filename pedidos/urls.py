from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.pedidos),
    url(r'^combinados/$', views.combinados),
    url(r'^montar/$', views.montar),
    url(r'^montar1$', views.montar1),
    url(r'^bebidas/$', views.bebidas),
    url(r'^finalizar$', views.finalizar),
    url(r'^pagamento$', views.pagamento),
    url(r'^dinheiro$', views.dinheiro),
    url(r'^cartao_debito$', views.cartao_debito),
    url(r'^cartao_credito$', views.cartao_credito),
    url(r'^final$', views.final),
    ]
