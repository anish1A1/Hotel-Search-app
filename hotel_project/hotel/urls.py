from django.urls import path
from .views import get_hotel, home
urlpatterns = [
    path('', home),
    path('api/gethotels/', get_hotel)
]
