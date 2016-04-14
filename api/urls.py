from django.conf.urls import url,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^users/(?P<pk>[0-9a-zA-Z]+)$',views.user_detail),
    url(r'^users$',views.users_list,name="user_list"),

    url(r'^search',views.search_documents),

    url(r'^documents/upload',views.upload_document),
    url(r'^documents/(?P<pk>[0-9a-zA-Z]+)$',views.document_detail),
    url(r'^documents$',views.document_list,name="doc_list"),

    url(r'',  views.home ),
]

urlpatterns=format_suffix_patterns(urlpatterns)