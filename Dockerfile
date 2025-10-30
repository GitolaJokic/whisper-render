FROM python:3.11-slim

# Systemabhängigkeiten
RUN apt-get update && apt-get install -y ffmpeg git && rm -rf /var/lib/apt/lists/*

# Whisper installieren
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git

WORKDIR /app

# Server starten
COPY server.py .
CMD ["python", "server.py"]
