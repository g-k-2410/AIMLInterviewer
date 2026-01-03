import requests
import os

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
HEADERS = {
    "Authorization": f"Bearer {os.environ['HF_TOKEN']}"
}

def transcribe_audio(audio_path):
    with open(audio_path, "rb") as f:
        r = requests.post(API_URL, headers=HEADERS, data=f)
    r.raise_for_status()
    return r.json()["text"]
