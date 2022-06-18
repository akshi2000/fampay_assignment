from django.core.paginator import Paginator
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from config import *
from .models import Video

import json


def paginateResponse(query_set, page):
    if page == None:
        page = 1
    page = int(page)
    pages = Paginator(query_set, NUMBER_OF_ITEMS_IN_A_PAGE)
    page = max(page, 1)
    page = min(page, pages.num_pages)
    data = json.loads(serialize("json", pages.get_page(page)))
    response = {
        "lastPage": pages.num_pages,
        "pageNumber": page,
        "numberOfItems": pages.count,
        "items": data,
    }
    return response


@api_view(["GET"])
def getVideoList(request):
    page = request.GET.get("page")
    query_set = Video.objects.all().order_by("published_date_time")
    response = paginateResponse(query_set, page)
    return Response(response)


@api_view(["GET"])
def searchVideoByTitle(request):
    page = request.GET.get("page")
    title_sub_string = request.GET.get("title")
    query_set = Video.objects.filter(video_title__icontains=title_sub_string).order_by(
        "published_date_time"
    )
    response = paginateResponse(query_set, page)
    return Response(response)


@api_view(["GET"])
def searchVideoByDescription(request):
    page = request.GET.get("page")
    description_sub_string = request.GET.get("description")
    query_set = Video.objects.filter(
        description__icontains=description_sub_string
    ).order_by("published_date_time")
    response = paginateResponse(query_set, page)
    return Response(response)
