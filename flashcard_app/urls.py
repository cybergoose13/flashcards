from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.newDeck),
    path('available', views.availableDeck),
    path('test', views.test)
]
