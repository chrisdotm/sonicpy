import json
from django.http import HttpResponse
from django.conf import settings
# Create your views here.

def home(request):
    return HttpResponse("woot")

def add_song(requets):
    if request.method == 'POST':
        return HttpResponse("YES")
    else:
        return HttpResponse("NO")



# anything that is called from /api/
# /api/get/
def api_get_music_home(request):
    if request.method == 'GET':
        return HttpResponse(json.dumps({"music_home": settings.MUSIC_HOME}))
    else:
        return HttpResponse("NO")

#/api/post/
def api_post_add_song(request):
    if request.method == 'POST':
        return HttpResponse("OK")
    else:
        return HttpResponse("NO")

def api_post_error_log(request):
    if request.method == 'POST':
        return HttpResponse("OK")
    else:
        return HttpResponse("NO")
#/api/put/

#/api/delete/


