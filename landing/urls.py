from django.conf.urls import url, include
from django.contrib import admin
from landing import views
from django.urls import path, re_path

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
    url(r'news/$', views.news, name='news'),
    url(r'contacts/$', views.contacts, name='contacts'),
    url(r'aboutus/$', views.aboutus, name='aboutus'),
    url(r'temprequest/$', views.temprequest, name='temprequest'),
    url(r'graphiki/$',views.graphiki, name='graphiki'),
    url(r'graph/$',views.graph, name='graph'),
    url(r'diagram/$', views.diagram, name='diagram'),
    url(r'example/$', views.example, name='example')
]