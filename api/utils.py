from api.models import YoutubeVideo
from typing import Dict, List
import requests, os
from dotenv import load_dotenv

load_dotenv()

query = os.getenv('query') or 'sports'

def getVideos (api_key: str, max_results: int = 20) -> Dict:
    url = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'key'           :   api_key,
        'part'          :   'snippet',
        'q'             :   query,
        'maxResults'    :   max_results,
        'order'         :   'date',
        'type'          :   'video'
    }
    
    data = {}

    response = requests.get(url, params = params)
    if response.status_code == 200 :
        response_json = response.json()
        data['videos'] = response_json['items']

    else :
        print(response.json())
        data['error_code'] = response.json()['error']['code']
        data['error_message'] = response.json()['error']['message']

    return data

def saveVideos (videos: List) -> None :
    try :
        for video in videos :
            YoutubeVideo.objects.get_or_create(
                video_id = video['id']['videoId'],
                title = video['snippet']['title'],
                channel_id = video['snippet']['channelId'],
                channel_title = video['snippet']['channelTitle'],
                description = video['snippet']['description'],
                thumbnail = video['snippet']['thumbnails']['default']['url'],
                published = video['snippet']['publishedAt'],
            )
        print(f'Added {len(videos)} new videos!')
    
    except Exception as e :
        print('ERROR:', e)
