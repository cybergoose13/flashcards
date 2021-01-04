from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('new', views.newCard, name= 'new'),
    path('addcard', views.addCard, name= 'addcard'),
    path('categories', views.categories, name= 'categories'),
    path('card/<str:category_id>', views.card, name= 'card_category'),
    path('test', views.test, name= "test")
]
