from __future__ import absolute_import, unicode_literals
from celery import Celery
from notification_service.settings import CELERY_BROKER_URL

app = Celery('notifications', broker=CELERY_BROKER_URL)

app.autodiscover_tasks()
