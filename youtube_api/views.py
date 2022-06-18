from urllib import response
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.serializers import serialize
import json

from googleapiclient.discovery import build
import googleapiclient.errors

# from youtube_api.tasks import fetch_lastest_youtube_videos
from config import *

from .models import Video


def paginateResponse(query_set, page):
    if page == None:
        page = 1
    page = int(page)
    pages = Paginator(query_set, NUMBER_OF_ITEMS_IN_A_PAGE)
    page = max(page, 1)
    page = min(page, pages.num_pages)
    data = json.loads(serialize("json", pages.get_page(page)))
    response = {
        "firstPage": 1,
        "lastPage": pages.num_pages,
        "pageNumber": page,
        "nextPage": min(page + 1, pages.num_pages),
        "previousPage": max(page - 1, 1),
        "numberOfItems": pages.count,
        "items": data,
    }
    return response


def getVideoList(request):
    # fetch_lastest_youtube_videos()
    page = request.GET.get("page")
    query_set = Video.objects.all().order_by("published_date_time")
    response = paginateResponse(query_set, page)
    return JsonResponse(response, status=200)


def searchVideoByTitle(request):
    page = request.GET.get("page")
    title_sub_string = request.GET.get("title")
    query_set = Video.objects.filter(video_title__icontains=title_sub_string).order_by(
        "published_date_time"
    )
    response = paginateResponse(query_set, page)
    return JsonResponse(response, status=200)


def searchVideoByDescription(request):
    page = request.GET.get("page")
    description_sub_string = request.GET.get("description")
    query_set = Video.objects.filter(
        description__icontains=description_sub_string
    ).order_by("published_date_time")
    response = paginateResponse(query_set, page)
    return JsonResponse(response, status=200)
