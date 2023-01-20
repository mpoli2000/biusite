from django.urls import path

from . import views

app_name = 'appdoku'
urlpatterns = [
    path('', views.index, name='index'),
    path('generar/', views.generar, name='generar')
]