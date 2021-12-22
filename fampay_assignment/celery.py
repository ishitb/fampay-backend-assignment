from __future__ import absolute_import, unicode_literals
from datetime import timedelta
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay_assignment.settings')

app = Celery('fampay_assignment')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Celery Beat
app.conf.beat_schedule = {
    'get_videos': {
        'task': 'api.tasks.get_videos',
        'schedule': timedelta(seconds=10)
    }
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))