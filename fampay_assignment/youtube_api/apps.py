from django.apps import AppConfig


class YoutubeApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "youtube_api"

    # def ready(self):
    #     pass
    #     # Import celery app now that Django is mostly ready.
    #     # This initializes Celery and autodiscovers tasks
    #     from fampay_assignment import celery
