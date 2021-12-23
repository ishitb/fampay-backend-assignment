from celery import shared_task
from .utils import getVideos, saveVideos
from .models import APIKey

# @shared_task
def get_videos () :
    api_keys = APIKey.objects.all()
    task_done = False
    for api_key in api_keys :

        if api_key.expired :
            print(api_key.name, 'has expired! Trying next key')
            continue

        data = getVideos(api_key=api_key.key)

        if data['error_code'] :
            print(f'Error {data["error_code"]}:', data['error_message'])

            if data['error_code'] == 403 :
                APIKey.objects.update_or_create(
                    id = api_key.id,
                    defaults = {
                        'expired': True
                    }
                )
            
            continue

        saveVideos(data['videos'])
        task_done = True

    if not task_done :
        print('All keys have expired, Please add more keys!')
