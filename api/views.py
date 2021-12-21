from django.db.models import query
from django.shortcuts import render
from .models import YoutubeVideo
from .serializers import YoutubeVideoSerializer
from rest_framework import generics

# Create your views here.
class YoutubeVideoView (generics.ListAPIView) :
    queryset = YoutubeVideo.objects.all().order_by('published')
    serializer_class = YoutubeVideoSerializer