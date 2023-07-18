from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movieman-index'),
    path('game', views.game, name='movieman-game'),
]