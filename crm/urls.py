from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_collaborateurs, name='liste_collaborateurs'),
    path('ajouter/', views.ajouter_collaborateur, name='ajouter_collaborateur'),
    path('accueil/', views.accueil, name='accueil'),
]
