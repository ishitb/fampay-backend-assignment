# FamPayExternship - Backend Assignment

# Youtube API using Django

## Description
> A server with an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

> > Server should call the YouTube API continuously in background (async) with some interval (say 10 seconds) for fetching the latest videos for a predefined search query and should store the data of vid eos (specifically these fields - Video title, description, publishing datetime, thumbnails URLs and any other fields you require) in a database with proper indexes. 

> >This task was achieved using the `celery` package.


> Support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.

> A dashboard to view the stored videos with filters and sorting options.

## Routes
- [GET] `/api/get-videos` - The endpoint returns the list of stored videos in a paginated form. The response is as below
```json
[
    {
        "id": "3d20beb9-d1d5-467d-bc8d-247058d5ed55",
        "video_id": "a88SZmG9Cx4",
        "title": "25 Marvel Actors Who Hated Their Costume (And 5 Who Loved Them)",
        "channel_id": "UC4qGmRZ7aLOLfVsSdj5Se2A",
        "channel_title": "TheThings",
        "description": "Pretty much every Marvel actor who's put on a hero or villain costume has had something to say about it. Usually terrible, horrible ...",
        "thumbnail": "https://i.ytimg.com/vi/a88SZmG9Cx4/default.jpg",
        "published": "2021-12-23T16:45:01Z"
    },
    {
        "id": "0098a315-5f15-4a26-b56c-53e609e61a02",
        "video_id": "G8BTQqXTEZE",
        "title": "MAFEX Wolverine Brown Version Medicom Marvel Comics X-Men Logan Action Figure Review",
        "channel_id": "UCF4CListjhpMJilZojUQVIA",
        "channel_title": "The Fwoosh",
        "description": "Medicom does it again! I know, I know, they have their issues every now and then, but this X-Men Brown Costume Wolverine is up ...",
        "thumbnail": "https://i.ytimg.com/vi/G8BTQqXTEZE/default.jpg",
        "published": "2021-12-23T16:00:07Z"
    }
]
```

- [GET] `/api/get-videos?limit=<integer>` - The endpoint returns the exact same result as above but with the option of a filter to get limited results.

- [GET] `/api/keys` - The endpoint returns the list of stores API Keys in the database. The response is as below
```json
[
    {
        "id": 2,
        "key": "1234567890",
        "name": "YOUTUBE 1",
        "created": "2021-12-22T20:11:27Z",
        "expired": false
    },
    {
        "id": 3,
        "key": "0987654321",
        "name": "youtube 2",
        "created": "2021-12-23T17:48:00Z",
        "expired": true
    }
]
```

- [POST] `/api/keys` - This endpoint is used to add more API Keys to the database, so that if one is expired, the next can be used.

- [GET] `/api/videos` - This is the dashboard created for viewing  the stored videos. The UI is built using [Tailwind CSS](https://tailwindcss.com/). The result is as below:
<img src='screenshots/dashboard.jpg' alt='Dashboard' width='1000' />

## Steps to run locally
### Requirements
- [Python](https://www.python.org/downloads/)
- [Redis](https://redis.io/download)

### Steps
- Download the zip or clone the repository
- Add the environment variables to the .env file according to .env.sample
- Run the Redis Server Locally or on the cloud, and add the broker url to the .env file
- Download the dependencies using the command:
```bash
    pip install -r requirements.txt
```
- Make the migrations for the django database with the commands:
```bash
python manage.py makemigrations
python manage.py migrate
```
- Create the superuser for Django
```bash
python manage.py createsuperuser
```
- Run the server locally using the command below. By default the server will be available on `http://127.0.0.1:8000`
```bash
python manage.py runserver
```
-Open another terminal in the same python environment and run the following command to run celery:
```bash
celery -A fampay_assignment beat -l INFO
```