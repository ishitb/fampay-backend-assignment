from django.db.models import query
from django.shortcuts import render
from rest_framework.response import Response
from .models import YoutubeVideo
from .serializers import YoutubeVideoSerializer
from rest_framework import generics

# Create your views here.
class YoutubeVideoView (generics.ListAPIView) :
    queryset = YoutubeVideo.objects.all().order_by('-published')
    serializer_class = YoutubeVideoSerializer

    def list (self, request) :
        # Default limit is 10
        limit = int(request.query_params.get('limit') or '10')

        queryset = self.get_queryset()[:limit]
        serializer = YoutubeVideoSerializer(queryset, many=True)
        return Response(serializer.data)
