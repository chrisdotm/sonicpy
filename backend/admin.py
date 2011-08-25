from django.contrib import admin
from sonicpy.backend.models import Artist, Song, Album

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
#admin.site.register(Play)
