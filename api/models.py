from django.db import models
import uuid

# Create your models here.

class YoutubeVideo(models.Model) :
    id              =   models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    video_id        =   models.CharField(max_length = 500, unique = True, null = True, blank = True)
    title           =   models.CharField(max_length = 500, null = True, blank = True)
    channel_id      =   models.CharField(max_length = 500, null = True, blank = True)
    channel_title   =   models.CharField(max_length = 500, null = True, blank = True)
    description     =   models.TextField(default = '', null = True, blank = True)
    thumbnail       =   models.CharField(max_length = 800, null = True, blank = True)
    published       =   models.DateTimeField()

    class Meta :
        db_table    =   'Videos'

    def __str__(self) -> str:
        return self.title