import os

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'film.settings.py')

app = Celery('cinema')
app.config_from_object('django.conf:settings.py', namespace='CELERY')
app.autodiscover_tasks()
