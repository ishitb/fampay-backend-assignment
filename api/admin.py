from django.contrib import admin
from .models import YoutubeVideo, APIKey

# Register your models here.
class YoutubeVideoAdmin (admin.ModelAdmin) :
    list_display = ('video_id', 'title', 'published')
    
class APIKeyAdmin (admin.ModelAdmin) :
    list_display = ('id', 'name', 'key', 'expired', 'created')

admin.site.register(YoutubeVideo, YoutubeVideoAdmin)
admin.site.register(APIKey, APIKeyAdmin)