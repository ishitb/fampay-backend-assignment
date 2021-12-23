from django.db.models import fields
from rest_framework import serializers
from .models import YoutubeVideo, APIKey

class YoutubeVideoSerializer(serializers.ModelSerializer) :
    class Meta:
        model = YoutubeVideo
        fields = '__all__'

class APIKeySerializer(serializers.ModelSerializer) :
    class Meta:
        model = APIKey
        fields = '__all__'