from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('/ws/chat/test', views.get_room_name)
]