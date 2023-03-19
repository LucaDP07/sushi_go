from django.urls import path
from . import views

urlpatterns = [
    path('', views.markets_all, name='markets'),
]