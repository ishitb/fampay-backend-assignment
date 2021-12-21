from django.db.models import base
from django.urls import path
from .views import YoutubeVideoView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('videos', YoutubeVideoView.as_view())
]