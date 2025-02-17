from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.item_create, name='item_create'),
    path('', views.item_list, name='item_list'),
    path('<int:pk>/', views.item_detail, name='item_detail'),
]
