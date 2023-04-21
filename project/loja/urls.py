from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('index', views.index, name='index'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logar', views.logar, name='logar'),
    path('pagina', views.pagina, name='pagina'),
    path('', views.inicio, name='inicio'),

]