from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # 使用consumers.ChatConsumer.as_asgi()为每个链接建立一个consumer实例
    path('ws/chat/test/', consumers.ChatConsumer.as_asgi())
]