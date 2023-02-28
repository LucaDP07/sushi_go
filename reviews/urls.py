from django.urls import path
from . import views

urlpatterns = [
    path(
        'testimonials/', views.Testimonials.as_view(), 
        name='testimonials'
        ),
    path(
        'testimonials/add/', views.AddTestimonial.as_view(),
        name='add_review'
        ),
    path(
        'testimonials/edit/<int:pk>/', views.EditTestimonial.as_view(),
        name='edit_review'
        ),
    path(
        'testimonials/delete/<int:pk>/', views.DeleteTestimonial.as_view(),
        name='delete_review'
        ),
]