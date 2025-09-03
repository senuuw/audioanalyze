import argparse
import yt_dlp
from download import download_audio

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help="Input video url")
    args = parser.parse_args()

    if not args.url:
        print("You must add url with --url")
        exit()
        
    video_url = "https://www.youtube.com/watch?v=RzrCv3ck3cg"
    audio_output_dir = 'audios'
    audio_path, audio_id = download_audio(video_url, audio_output_dir)
    print(f"Audio_path: {audio_path}, Audio_id {audio_id}")

