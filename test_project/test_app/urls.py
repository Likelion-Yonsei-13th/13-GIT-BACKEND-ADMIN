from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.item_create, name='item_create'),
]
