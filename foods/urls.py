from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_foods, name='foods'),
    path('<int:food_id>/', views.food_detail, name='food_detail'),
    path('add/', views.add_food, name='add_food'),
    path('edit/<int:food_id>/', views.edit_food, name='edit_food'),
    path('delete/<int:food_id>/', views.delete_food, name='delete_food'),
]
