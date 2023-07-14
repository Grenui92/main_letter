from django.urls import re_path

from .consumers import MainLetterConsumer
websocket_urlpatterns = [
    re_path('main_letter', MainLetterConsumer.as_asgi())
]