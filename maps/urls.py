from django.urls import path
from . import views

urlpatterns = [
    path('maps/', views.MapView.as_view(), name='maps-list'),
    path('maps/<int:map_id>/', views.MapView.as_view(), name='map-detail'),
    path('maps/<int:map_id>/navigation/', views.MapNavigationView.as_view(), name='map-navigation'),
]