from rest_framework.response import Response
from .models import YoutubeVideo, APIKey
from .serializers import YoutubeVideoSerializer, APIKeySerializer
from rest_framework import generics, viewsets, mixins

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

class APIKeyViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin) :
    serializer_class = APIKeySerializer
    queryset = APIKey.objects.all()