from __future__ import unicode_literals
import youtube_dl

link = 'eneter_link'

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
