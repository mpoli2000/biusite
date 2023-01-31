from django.urls import path

from . import views

app_name = 'appdoku'
urlpatterns = [
    path('', views.index, name='index'),
    path('generar/', views.generar, name='generar'),
    path('tablero/<int:tablero_id>', views.tablero, name='tablero'),
    # path('tablero/<int:tablero_id>/evaluar', views.evaluar, name='evaluar'),
    path('grilla', views.grilla, name='grilla'),
]