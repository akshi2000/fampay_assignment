from celery import Celery
import os
from celery.schedules import crontab

from celery import Celery

# from youtube_api.tasks import fetch_lastest_youtube_videos
# from youtube_api.models import Video
from config import *

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fampay_assignment.settings")

app = Celery("fampay_assignment")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


# @app.task
# def fetch_lastest_youtube_videos1():
#     print("EXECUTED")
#     api_service_name = "youtube"
#     api_version = "v3"
#     try:
#         youtube = build(
#             api_service_name,
#             api_version,
#             developerKey=API_KEY,
#         )

#         request = youtube.search().list(
#             part="id,snippet",
#             type="video",
#             publishedAfter=PUBLISHED_AFTER_DATE_TIME,
#             order="date",
#             topicId=TOPIC,
#         )
#         response = request.execute()
#         videos = response["items"]
#         for video in videos:
#             snippet = video["snippet"]
#             video_obj = Video()
#             video_obj.video_id = video["id"]["videoId"]
#             video_obj.video_title = snippet["title"]
#             video_obj.thumbnail_url = snippet["thumbnails"]["default"]["url"]
#             video_obj.published_date_time = snippet["publishTime"]
#             video_obj.description = snippet["description"]
#             video_obj.save()
#     except Exception as e:
#         print("ERROR", e)


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(
#         10.0, fetch_lastest_youtube_videos1.s(), name="add every 10"
#     )

#     # Calls test('world') every 30 seconds
#     sender.add_periodic_task(30.0, fetch_lastest_youtube_videos1.s(), expires=10)

#     # Executes every Monday morning at 7:30 a.m.
#     sender.add_periodic_task(
#         crontab(hour=7, minute=30, day_of_week=1), fetch_lastest_youtube_videos1.s()
#     )
