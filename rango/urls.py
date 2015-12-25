from django.conf.urls import patterns, url
from rango import views

urlpatterns = [
    url(r'^$', views.inex, name='index'),
    url(r'^about', views.about, name ='about'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
]
