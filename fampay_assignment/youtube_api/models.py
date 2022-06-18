from django.db import models


class Video(models.Model):
    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "published_date_time",
                ]
            ),
            models.Index(
                fields=[
                    "video_title",
                ]
            ),
            models.Index(
                fields=[
                    "description",
                ]
            ),
        ]

    video_id = models.CharField(max_length=50, unique=True)
    video_title = models.CharField(max_length=100)
    published_date_time = models.DateTimeField()
    thumbnail_url = models.URLField(null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.video_title
