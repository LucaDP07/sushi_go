from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('foods/', include('foods.urls')),
    path('basket/', include('basket.urls')),
    path('contact/', include('contact.urls')),
    path('reviews/', include('reviews.urls')),
    path('order/', include('order.urls')),
    path('profile/', include('profiles.urls')),
    path('markets/', include('markets.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'sushi_go.views.handler404'
