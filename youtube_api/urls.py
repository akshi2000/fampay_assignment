from django.urls import path
from . import views

urlpatterns = [
    path("getVideos", views.getVideoList),
    path("searchVideo", views.getVideoList),
]
