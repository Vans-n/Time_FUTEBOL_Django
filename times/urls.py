from django.urls import path
from .views import lista_times

urlpatterns = [
    path('', lista_times, name='lista_times'),
]