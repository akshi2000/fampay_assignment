from django.urls import path
from . import views

urlpatterns = [
    path("getVideos", views.getVideoList),
    path("searchVideoTitle", views.searchVideoByTitle),
    path("searchVideoDescription", views.searchVideoByDescription),
]
