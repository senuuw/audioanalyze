import yt_dlp
import os


def download_audio(video_url, output_dir):

    with yt_dlp.YoutubeDL({"quiet": True, "noplaylist": True}) as ydl:
        meta = ydl.extract_info(video_url, download=False)
        audio_id = meta["id"]

    audio_file_name = audio_id + ".m4a"

    if audio_file_name in os.listdir(output_dir):
        cwd = os.getcwd()
        audio_path = os.path.join(cwd, output_dir, audio_file_name)
        return audio_path, audio_id
    

    yt_opts = {
        'format': 'm4a/bestaudio/best',
        'paths' : {'home' : output_dir},
        "outtmpl": r"%(id)s.%(ext)s",
        "noplaylist": True,
        'postprocessors': [{  
            'key': 'FFmpegExtractAudio'
        }]
    }

    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        info = ydl.extract_info(video_url, download=True)
        audio_path = info['requested_downloads'][0]['filepath']

    return audio_path, audio_id

if __name__ == '__main__':
    youtube_url = "https://www.youtube.com/watch?v=fvOyAAjVJEk"
    output_dir = r"audios"
    audio_path, audio_id = download_audio(youtube_url, output_dir)
    print(f"Audio Path: {audio_path}, Audio_id: {audio_id}")
