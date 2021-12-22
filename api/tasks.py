from celery import shared_task
import os
from .utils import getVideos, saveVideos

@shared_task
def get_videos () :
    api_key = os.getenv('YOUTUBE_API_KEY')
    data = getVideos(api_key=api_key)
    saveVideos(data['videos'])