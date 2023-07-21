from celery import Celery
from django.conf import settings

default_celery_app = Celery("tasks")

default_celery_app.config_from_object("django.conf:settings", namespace="CELERY")
default_celery_app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)