import argparse
import yt_dlp


parser = argparse.ArgumentParser()
parser.add_argument('--url', help="Input video url")
args = parser.parse_args()

if not args.url:
    print("You must add url with --url")
    exit()


yt_opts = {
    'format': 'm4a/bestaudio/best',
    'paths' : {'home' : 'audios'},
    'postprocessors': [{  
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a'
    }]
}

with yt_dlp.YoutubeDL(yt_opts) as ydl:
    info = ydl.extract_info(args.url, download=True)

    audio_path = info['requested_downloads'][0]['filepath']
    print("Saved file:", audio_path)
