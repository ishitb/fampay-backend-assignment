from django.contrib import admin
from .models import YoutubeVideo

# Register your models here.
class YoutubeVideoAdmin (admin.ModelAdmin) :
    list_display = ('video_id', 'title', 'published')

admin.site.register(YoutubeVideo, YoutubeVideoAdmin)