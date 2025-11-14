import argparse
import yt_dlp
from download import download_audio
from analyze import count_terms
from transcribe import transcribe_audio
import heapq
if __name__ == "__main__":
        
    video_url = "https://www.youtube.com/watch?v=NF5Cu6UJiCs"
    audio_output_dir = 'audios'
    audio_path, audio_id = download_audio(video_url, audio_output_dir)
    print(f"Audio_path: {audio_path}, Audio_id {audio_id}")
    pickle_path = transcribe_audio(audio_path)
    print(pickle_path)
    clean_text, card_map, extra_map = count_terms(pickle_path)
    
    card_sorted = heapq.nlargest(5, card_map, key=card_map.get)
    extra_sorted = heapq.nlargest(5, extra_map, key=extra_map.get)
    
    print("Top 5 Cards said:")
    for card in card_sorted:
        print(f" {card}: {card_map[card]}")

    print("Top 5 Gameplay words said:")
    for word in extra_sorted:
        print(f" {word}: {extra_map[word]}")

