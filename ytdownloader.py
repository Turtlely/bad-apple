from __future__ import unicode_literals
import youtube_dl


def download(url):
    with youtube_dl.YoutubeDL({}) as ydl:
        ydl = {}
        #ydl.download(['https://www.youtube.com/watch?v=9lNZ_Rnr7Jc'])
        #ydl.download(['https://www.youtube.com/watch?v=UnIhRpIT7nc'])
        ydl.download([url])

