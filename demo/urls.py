from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('book', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('first', views.first),
]
