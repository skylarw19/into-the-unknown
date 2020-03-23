from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('places/', views.places_index, name='index'),
    path('places/<int:place_id>/', views.places_detail, name='places_detail')
]
