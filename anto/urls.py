from django.urls import path

from . import views

app_name = 'anto'
urlpatterns = [
    path('', views.index, name='index'),
    path('clases/', views.clases, name='clases'),

]