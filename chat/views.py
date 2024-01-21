from django.shortcuts import render
from django.http import (
    Http404,
    HttpResponse,
    HttpResponsePermanentRedirect,
    HttpResponseRedirect,
)
# Create your views here.
def index(request):
    return render(request, 'chat/index.html')


def get_room_name(request):
    print(request)
    return HttpResponse('111111')