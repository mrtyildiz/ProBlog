from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('blog/<int:pk>/', views.blog_list, name='blog_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
