import os, torch, whisperx
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()
hf_token = os.getenv("HF_TOKEN")
assert hf_token, "HF_TOKEN is missing. Set HF_TOKEN=... in your .env"

print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("cuDNN:", torch.backends.cudnn.version())

device = "cuda" if torch.cuda.is_available() else "cpu"
compute_type = "float16" if device == "cuda" else "float32"

audio_file = r"C:\Users\Senu9\Documents\Projects\audioanalyze\audios\2012 Didn't Happen [kcc_KAhwpa0].m4a"
model_dir  = r"C:\Users\Senu9\Documents\Projects\audioanalyze\models"

login(token=hf_token)

model = whisperx.load_model("large-v2", device, compute_type=compute_type, download_root=model_dir)
audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=16)
print("Detected language:", result["language"])
print("First segment pre-align:", result["segments"][0] if result["segments"] else "None")

model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
print("First segment post-align:", result["segments"][0] if result["segments"] else "None")

try:
    diarize_model = whisperx.diarize.DiarizationPipeline(use_auth_token=hf_token, device=device)
except Exception as e:
    raise RuntimeError(
        "Failed to init diarization. Make sure your HF token has access to "
        "'pyannote/segmentation-3.0' and 'pyannote/speaker-diarization-3.1', "
        "and that you ran huggingface_hub.login(token=...)."
    ) from e


# diarize_segments = diarize_model(audio, min_speakers=2, max_speakers=2)
diarize_segments = diarize_model(audio)

result = whisperx.assign_word_speakers(diarize_segments, result)
print("Diarization segments (head):", diarize_segments[:3])
print("First aligned+speaker segment:", result["segments"][0] if result["segments"] else "None")
