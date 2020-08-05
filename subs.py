import sys
import hashlib
import os
import requests

#Function to calculate HASH from video file
def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize,os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

if len(sys.argv) == 3:
    video = sys.argv[1]     #Passing-Video
    subname= sys.argv[2]    #Passing-Subtitle-File-Name
    hash = get_hash(video)
    r = requests.get('http://api.thesubdb.com/?action=download&hash={}&language=en'.format(hash), headers={'User-Agent': 'SubDB/1.0 (subsy/0.1; https://github.com/iamnihal/extractor)'})
    with open(subname, mode='w') as fd:
        fd.write(r.text)
else:
    print("\nUsage:\npython subsy.py <Video> <Subtitle_Name>")
