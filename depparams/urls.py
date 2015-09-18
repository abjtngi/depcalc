from django.conf.urls import url
from depparams import views

urlpatterns = [
    url(r'^createarticle/$', views.article_creation_home, name='article_creation_home'),
    url(r'^createarticle/save/$', views.ArticleCreationHomeSave.as_view(), name='article_creation_home_save'),
    url(r'^createarticle/addattributes/(?P<article_id>\d+)$', views.article_creation_add_attributes,
        name='article_creation_add_attributes'),
    url(r'^createarticle/addattributes/save$', views.ArticleCreationAddAttributeSave.as_view(),
        name='article_creation_add_attributes_save'),
    url(r'^createarticle/adddepreciationparams/(?P<article_id>\d+)$$', views.article_creation_add_depparams,
        name='article_creation_add_depparams'),
]

