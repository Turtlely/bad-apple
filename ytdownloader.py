from __future__ import unicode_literals
import youtube_dl
import os

os.chdir('VIDEOS')
def download(url):
    with youtube_dl.YoutubeDL({}) as ydl:
        ydl.download([url])