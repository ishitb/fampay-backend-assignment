from django.db.models import fields
from rest_framework import serializers
from .models import YoutubeVideo

class YoutubeVideoSerializer(serializers.ModelSerializer) :
    class Meta:
        model = YoutubeVideo
        fields = '__all__'