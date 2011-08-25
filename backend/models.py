from django.db import models
from django.contrib.auth import models as auth_models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    mb_id = models.CharField(max_length=40, primary_key=True)

    def __unicode__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=255)
    mb_id = models.CharField(max_length=40, primary_key=True)
    artist_id = models.ManyToManyField(Artist)

    def __unicode__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=255)
    mb_id = models.CharField(max_length=40, primary_key=True)
    artist_id = models.ForeignKey(Artist)
    album_id = models.ForeignKey(Album)

    def __unicode__(self):
        return self.name


#class CustomUser(auth_models.User):
#    plays = models.IntegerField()
#
#class Play(self.CustomUser):
#    user = models.ForeignKey(CustomUser)
#    song = models.ForeignKey(Song)
#    play_date = models.DateTimeField()
#
#    def __unicode__(self):
#        return self.user
#
#    class Meta:
#        order_with_respect_to = 'play_date'
