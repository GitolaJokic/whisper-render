from flask import Flask, request, jsonify
import whisper
import requests
import os

app = Flask(__name__)
model = whisper.load_model("small")  # Kleinere Version, läuft schneller auf Free-Tier

@app.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.json
    audio_url = data.get("audio_url")
    if not audio_url:
        return jsonify({"error": "No audio_url provided"}), 400

    # Audio herunterladen
    audio_file = "temp_audio.ogg"
    r = requests.get(audio_url)
    with open(audio_file, "wb") as f:
        f.write(r.content)

    # Transkription
    result = model.transcribe(audio_file)
    text = result.get("text", "")

    # Temp-Datei löschen
    os.remove(audio_file)

    return jsonify({"text": text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
