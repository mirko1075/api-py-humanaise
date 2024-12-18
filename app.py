from flask import Flask, request, jsonify
import whisper
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
model = whisper.load_model("large")

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["file"]
    audio_path = f"/tmp/{file.filename}"
    file.save(audio_path)
    result = model.transcribe(audio_path)
    return jsonify({"transcription": result["text"]})

@app.route("/translate", methods=["POST"])
def translate():
    text = request.json.get("text")
    target_lang = request.json.get("target_lang", "EN")
    deepl_api_url = "https://api-free.deepl.com/v2/translate"
    headers = {"Authorization": f"Bearer {DEEPL_API_KEY}"}
    data = {"text": text, "target_lang": target_lang}
    response = requests.post(deepl_api_url, headers=headers, data=data)
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
