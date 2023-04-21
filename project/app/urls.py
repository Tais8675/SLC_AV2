from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.index, name="index"),
    path("<int:app_id>", views.app, name="app"),
    path('inicio', views.inicio, name='inicio'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logar', views.logar, name='logar'),
    path('pagina', views.pagina, name='pagina'),
    

    
]
