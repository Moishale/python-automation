from __future__ import unicode_literals
import youtube_dl

link = 'https://www.youtube.com/watch?v=nqdMYI-bUp8'

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
