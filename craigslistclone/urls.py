from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('register/',  views.register, name="register"),
    path('login/',  views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('listings/', views.listings, name="listings"),
    path('listings/upload', views.upload_listing, name="upload_image"),
    path('home/', views.home, name="home")
]

# Serves media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)