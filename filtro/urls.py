from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anuncio/<int:id>', views.anuncioView, name="anuncio-view"),
    path('anunciar', views.newAnuncio, name="newAnuncio")
]
