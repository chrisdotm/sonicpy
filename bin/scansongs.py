import os
import urllib
import json
import sys
import mutagen


api_host = "localhost:8000"


def main():
    music_home = {'music_home': None}
    try:
        music_home_fh = urllib.urlopen(
                "http://%s/api/get/music_home" % api_host)
        music_home = json.loads(music_home_fh.read())
    except Exception, e:
        logerror(e)

    music_home_path = music_home['music_home']
    scan_dir(music_home_path)


def scan_dir(path):
    if os.path.isdir(path):
        for root, dirs, files in os.walk(path):
            parse_tree(root, dirs, files)
    else:
        logerror("%s is not a valid path" % path)
        sys.exit(1)


def parse_tree(root, dirs, files):
    if len(dirs) == 0:
        for f in files:
            full_path = os.path.join(root, f)
            try:
                data = mutagen.File(full_path, easy=True)
                if data is not None:
                    add_song(data, full_path)
            except Exception, e:
                logerror(e)


def add_song(song_data, path):
    try:
        print "adding %s" % path
        upload = {
                'data': json.dumps(dict(song_data)),
                'path': json.dumps(path)}
        params = urllib.urlencode(upload)
        fh = urllib.urlopen("http://%s/api/post/add_song" % api_host, params)
        print fh.read()
    except Exception, e:
        logerror(e)


def logerror(error_msg):
    real_msg = "ERR: %s --- %s" % (os.path.basename(__file__), error_msg)
    params = urllib.urlencode({'error_message': real_msg})
    try:
        fh = urllib.urlopen("http://%s/api/post/error_log" % api_host, params)
        fh.read()
    except Exception, e:
        pass  # nothing really left to do now


if __name__ == '__main__':
    main()
