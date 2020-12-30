from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.newCard),
    path('addcard', views.addCard),
    path('catagories', views.catagories),
    path('test', views.test)
]
