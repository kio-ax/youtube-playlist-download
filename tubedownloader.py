import youtube_dl

def down():
    vid_url=input("Paste your youtube playlist here: ")
    info=youtube_dl.YoutubeDL().extract_info(
        url=vid_url, download=false
    )
    fname=f"{info['title']}.mp3"
    opt={
        'format':'bestaudio/best',
        'keepvideo':false,
        'outtmpl':fname,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
        
    }
    with youtube_dl.YoutubeDL(opt) as ydl:
        ydl.download([info['webpage_url']])
