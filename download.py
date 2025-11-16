import yt_dlp

def download_audio(video_id):

    video_url = "https://www.youtube.com/watch?v=" + video_id
    
    yt_opts = {
        'format': 'm4a/bestaudio/best',
        'paths' : {'home' : 'audios'},
        "outtmpl": r"%(id)s.%(ext)s",
        "noplaylist": True,
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio'
        }]
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        audio_path = info['requested_downloads'][0]['filepath']

    return audio_path