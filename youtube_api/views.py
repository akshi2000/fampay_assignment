from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# import google_auth_oauthlib.flow
from googleapiclient.discovery import build
import googleapiclient.errors

from config import *

from .models import Video

# Create your views here.

# to be implemented as a celery task
def fetch_lastest_youtube_videos():
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
            publishedAfter="2020-01-01T00:00:00Z",
            order="date",
        )
        response = request.execute()
        videos = response["items"]
        for video in videos:
            snippet = video["snippet"]
            title = snippet["title"]
            thumbnail_url = snippet["thumbnails"]["default"]["url"]
            channel_title = snippet["channelTitle"]
            publishTime = snippet["publishTime"]
            print("Video Details")
            print(title, thumbnail_url, channel_title, publishTime)
    except:
        print("ERROR")


def getVideoList(request):
    fetch_lastest_youtube_videos()
    videos = Video.objects()
    print(videos)
    # return JsonResponse(response, status=200)
    return HttpResponse("Videos Data in Json")


def searchVideo(request):
    return HttpResponse("Searched Videos in JSON")
