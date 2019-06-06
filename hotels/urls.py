from django.urls import path
from . import views


urlpatterns = [
    path('', views.hotel_home, name='hotel_home'),
    path('<region>/', views.hotel_list, name='hotel_list'),
    path('hotel/<hotel_id>/', views.hotel_detail, name='hotel_detail'),
    path('ajax_calls/search/', views.autocompleteModel, name='autocomplete'),
]