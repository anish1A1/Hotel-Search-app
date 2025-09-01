from django.urls import path
from .views import get_hotel
urlpatterns = [
    path('api/gethotels/', get_hotel)
]
