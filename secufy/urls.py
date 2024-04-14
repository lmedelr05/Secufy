from django.urls import path
from . import views  # Importa todo el módulo de vistas

urlpatterns = [
    path('', views.home_view, name='home'),
    path('nosotros/', views.nosotros_view, name='nosotros'),
    path('contacto/', views.contacto_view, name='contacto'),
    path('appMovil/', views.appMovil_view, name='appMovil'),
    path('appWeb/', views.appWeb_view, name='appWeb'),
    path('deskopIoT/', views.deskopIoT_view, name='deskopIoT'),
    # Otras URLs
]
