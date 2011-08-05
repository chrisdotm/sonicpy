#!/bin/env python

'''
' Author: Chris McCoy
' ./lib/api.py
' This is module contians the final hooks for the sonicpy app
'''


def get_songs(album_id):
    """Return the list of songs for a given album """
    pass

def get_albums():
    """Return the list of albums available"""
    pass

def get_artists():
    """Return the list of artists available"""
    pass

def get_artists_by_letter(first_letter):
    """Return the list of artist by given first letter"""
    pass

def get_artist_by_id(artist_id):
    """Return the artist identified by the given id"""
    pass

def get_plays_by_user(user_id):
    """Return the number of plays for a given user"""
    pass

def get_plays_by_song(song_id):
    """Return the number of plays for a given song"""
    pass

def get_plays_by_artist(artist_id):
    """Return the number of plays for a given artist"""
    pass

def get_plays_by_album(album_id):
    """Return the number of plays for a given album"""
    pass

def get_users():
    """Return the list of users probably only accessable by admin"""
    pass

def login(user_name, user_password):
    """Return the api token or None for the user that logs in"""
    pass

def logout(user_token):
    """Returns true if the api token is active false if not"""
    pass


