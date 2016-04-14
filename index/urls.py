from django.conf.urls import url, include
from . import views

urlpatterns = [
    #url(r'document/(?P<pk>[0-9]+)$', views.view_document),
    url(r'^document/(?P<pk>[0-9a-zA-Z]+)$',views.view_document),
    url(r'', views.home),
]
