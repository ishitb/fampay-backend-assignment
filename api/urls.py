from django.db.models import base
from django.urls import path
from .views import YoutubeVideoView, APIKeyViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('api-keys', APIKeyViewSet, basename = 'API Keys')

urlpatterns = router.urls + [
    path('videos', YoutubeVideoView.as_view())
]