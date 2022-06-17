from pyexpat import model
from django.db import models

# Create your models here.


class Video(models.Model):
    class Meta:
        indexes = [
            models.Index(
                fields=[
                    "published_date_time",
                ]
            ),
        ]

    video_id = models.IntegerField()
    video_title = models.CharField(max_length=100)
    published_date_time = models.DateTimeField()
    thumbnail_url = models.URLField(null=True)
    description = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.video_title
