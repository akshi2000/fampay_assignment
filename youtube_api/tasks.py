from __future__ import absolute_import, unicode_literals
from celery import shared_task
import datetime
from googleapiclient.discovery import build
import googleapiclient.errors

from config import *


@shared_task
def add(x, y):
    return x + y


@shared_task
def fetch_lastest_youtube_videos():
    api_service_name = "youtube"
    api_version = "v3"
    try:
        youtube = build(
            api_service_name,
            api_version,
            developerKey=API_KEY,
        )

        request = youtube.search().list(part="id,snippet")
        response = request.execute()
        print(type(response))
        print(response)
    except:
        print("ERROR")
