from flask import Flask, request, jsonify
import whisper
import requests

app = Flask(__name__)
model = whisper.load_model("small")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    data = request.json
    audio_url = data.get("audio_url")
    if not audio_url:
        return jsonify({"error": "No audio_url provided"}), 400

    # Audio herunterladen
    r = requests.get(audio_url)
    with open("temp.ogg", "wb") as f:
        f.write(r.content)

    # Transkription
    result = model.transcribe("temp.ogg")
    return jsonify({"text": result["text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
