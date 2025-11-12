import os, torch, whisperx
from dotenv import load_dotenv
from huggingface_hub import login
import pickle


load_dotenv()
hf_token = os.getenv("HF_TOKEN")
assert hf_token, "HF_TOKEN is missing. Set HF_TOKEN=... in your .env"

audio_file = r"C:\Users\Senu9\Documents\Projects\audioanalyze\audios\US_U0fsSBPM.m4a"
model_dir  = r"C:\Users\Senu9\Documents\Projects\audioanalyze\models"
filename_id = os.path.basename(audio_file)[:-4]
output_path = os.path.join("transcripts", filename_id + ".pkl")


print("CUDA available:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    print("cuDNN:", torch.backends.cudnn.version())

device = "cuda" if torch.cuda.is_available() else "cpu"
compute_type = "float16" if device == "cuda" else "float32"

login(token=hf_token)

model = whisperx.load_model("large-v2", device, compute_type=compute_type, download_root=model_dir)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=16)

output_path = "transcripts\ " + filename_id + ".pkl"
with open(output_path, 'wb') as file:
    pickle.dump(result['segments'], file)
