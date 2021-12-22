from celery import shared_task
import os
from .utils import getVideos, saveVideos
from .models import APIKey

@shared_task
def get_videos () :
    print('Hello')
    # api_keys = APIKey.objects.all()
    # for api_key in api_keys :
    #     # print(api_key.last_expired)
    #     # print(api_key.created)
    #     print(dir(api_key))

        # data = getVideos(api_key=api_key)
        # saveVideos(data['videos'])