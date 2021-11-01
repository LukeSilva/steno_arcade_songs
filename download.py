import youtube_dl
import subprocess
import os.path
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'vorbis',
        'preferredquality': '192',
    }],
}

songs = [
    ('http://www.youtube.com/watch?v=0a6j3rv1PFk', '我會守在這裡'),
    ('https://www.youtube.com/watch?v=BiiwclhI5Y8', '平凡的一天')
]

for url, out_name in songs:
    ydl_opts['outtmpl'] = '{}/{}.%(ext)s'.format(out_name, out_name)
    if not os.path.isfile('{}/{}.ogg'.format(out_name,out_name)):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    else:
        print("{} already exists, skipping".format(out_name))

subprocess.call(['ffmpeg',  '-ss', '22', '-i', '平凡的一天/平凡的一天.ogg', '-acodec', 'copy', '平凡的一天/平凡的一天_cut.ogg'])