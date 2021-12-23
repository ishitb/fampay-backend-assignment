from django.db.models import base
from django.urls import path
from .views import YoutubeVideoView, APIKeyViewSet, videos_template
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('keys', APIKeyViewSet, basename = 'API Keys')

urlpatterns = router.urls + [
    path('get-videos', YoutubeVideoView.as_view()),
    path('videos', videos_template)
]