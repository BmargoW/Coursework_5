import os
from datetime import timedelta

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")


# app.conf.beat_scheduler = 'django_celery_beat.schedulers:DatabaseScheduler'

app.conf.beat_schedule = {
    "send_mail_about_hubit": {
        "task": "habit.tasks.send_mail_about_hubit",
        "schedule": timedelta(seconds=10),
    },
    "send_daily_hubit": {
        "task": "habit.tasks.send_daily_habit",
        "schedule": crontab(hour=8, minute=0),
    },
}

app.autodiscover_tasks()


app.autodiscover_tasks()
