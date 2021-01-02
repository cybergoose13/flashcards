from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.newCard),
    path('addcard', views.addCard),
    path('categories', views.categories),
    path('card/<str:category_id>', views.card),
    path('test', views.test)
]
