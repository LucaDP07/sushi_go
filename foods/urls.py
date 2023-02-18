from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_foods, name='foods'),
    path('<food_id>', views.food_detail, name='food_detail'),
]