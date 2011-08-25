from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sonicpy.views.home', name='home'),
    # url(r'^sonicpy/', include('sonicpy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'backend.views.home'),
    url(r'^api/get/music_home', 'backend.views.api_get_music_home'),
    url(r'^api/post/add_song', 'backend.views.api_post_add_song'),
    url(r'^admin/', include(admin.site.urls)),
)
