from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.extrato),
    url(r'^diario/$', views.diario),
    ]
