from django.urls import path
from . import views

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),

    # Карты
    path('maps/', views.maps_list, name='maps_list'),
    path('maps/<slug:slug>/', views.map_detail, name='map_detail'),
]
