from django.urls import path
from . import views

urlpatterns = [
    path('', views.explorer_view, name='explorer'),
    path('filtros/', views.filtros, name='filtros'),
]