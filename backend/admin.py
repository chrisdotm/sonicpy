from django.contrib import admin
from sonicpy.backend.models import CustomUser, Artist, Song, Album, Play

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Play)
