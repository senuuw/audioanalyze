from download import download_audio
from analyze import analyze_transcript
from transcribe import transcribe_audio
import heapq
import yt_functions
import os

def main():

    video_id = yt_functions.check_latest_video()

    if yt_functions.is_vod(video_id):
        return None
    
    if (video_id + ".pkl") in os.listdir("transcripts"):
        return None

    audio_path = download_audio(video_id)
    pickle_path = transcribe_audio(audio_path)
    card_map, extra_map = analyze_transcript(pickle_path)
    
    yt_functions.post_comment(video_id, card_map, extra_map)



if __name__ == "__main__":
    main()

