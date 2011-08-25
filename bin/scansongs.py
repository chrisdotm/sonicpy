import os
import urllib
import json
import sys
import mutagen

def main():
    music_home = {'music_home': None}
    try:
        music_home_fh = urllib.urlopen("http://localhost:8000/api/get/music_home")
        music_home = json.loads(music_home_fh.read())
    except Exception, e:
        print e

    music_home_path = music_home['music_home']
    scan_dir(music_home_path)

def scan_dir(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            parse_tree(root, dirs, files)
    else:
        sys.exit(1)

def parse_tree(root, dirs, files):
    if len(dirs) == 0:
        for f in files:
            full_path = os.path.join(root, f)
            data = mutagen.File(full_path, easy=True)
            if data is not None:
                add_song(data, full_path)

def add_song(song_data, path):
    try:
        print "adding %s" % path
        upload = {
                'data': json.dumps(dict(song_data)),
                'path': json.dumps(path)}
        params = urllib.urlencode(upload)
        fh = urllib.urlopen("http://localhost:8000/api/post/add_song", params)
        print fh.read()
    except Exception, e :
        print e

if __name__ == '__main__':
    main()
#os.environ['DJANGO_SETTINGS_MODULE'] = 'sonicpy.settings'
#print settings.MUSIC_HOME
#import sys
#import os
#thisdir = os.path.dirname(os.path.abspath(__file__))

#sys.path.append(os.path.join(thisdir, '../'))

#print sys.path
