from celery import shared_task
from googleapiclient.discovery import build
import googleapiclient.errors

from .models import Video
from config import *


@shared_task
def fetch_lastest_youtube_videos():
    print("Fetching Videos....")
    api_service_name = "youtube"
    api_version = "v3"
    try:
        youtube = build(
            api_service_name,
            api_version,
            developerKey=API_KEY,
        )

        request = youtube.search().list(
            part="id,snippet",
            type="video",
            publishedAfter=PUBLISHED_AFTER_DATE_TIME,
            order="date",
            topicId=TOPIC,
        )
        response = request.execute()
        videos = response["items"]
        for video in videos:
            snippet = video["snippet"]
            video_obj = Video()
            video_obj.video_id = video["id"]["videoId"]
            video_obj.video_title = snippet["title"]
            video_obj.thumbnail_url = snippet["thumbnails"]["default"]["url"]
            video_obj.published_date_time = snippet["publishTime"]
            video_obj.description = snippet["description"]
            video_obj.save()
    except Exception as e:
        print("ERROR", e)
