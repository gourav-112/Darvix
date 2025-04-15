# 🧠 AI-Powered Django Backend

This Django project provides two core AI-powered features:

1. 🎙️ **Audio Transcription with Diarization** – Transcribes uploaded audio and identifies "who spoke when" using `whisperx`.
2. ✍️ **AI Title Suggestions for Blog Posts** – Generates smart title suggestions based on blog content using NLP.

---

## 🚀 Features

### 1. Audio Transcription with Diarization

- Accepts audio files via an API.
- Transcribes speech to text.
- Performs **speaker diarization** (who said what and when).
- Returns structured JSON output.
- Supports multilingual transcription (via WhisperX).

### 2. AI Title Suggestions for Blogs

- Accepts blog content via POST request.
- Uses NLP (transformers) to generate 3 smart title suggestions.
- Returns a JSON list of suggestions.

---

## 🛠️ Tech Stack

- **Backend:** Django 5
- **Transcription:** [`whisperx`](https://github.com/m-bain/whisperx), PyTorch
- **NLP:** Hugging Face `transformers`
- **Containerization:** Docker & Docker Compose

---

## 📦 Installation

### 1. Clone the Repo

```bash
git clone https://github.com/gourav-112/darvix.git
cd darvix
python -m venv venv
.\venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

🐳 Run with Docker
Build & Start
```bash
docker-compose up --build
```
The server will be running at:
📍 http://localhost:8000/

📡 API Endpoints
/api/transcribe/ – Audio Transcription
Method: POST
Payload: multipart/form-data

```bash
curl -X POST -F "audio=@your_audio_file.mp3" http://localhost:8000/api/transcribe/
```

Response:
```json
{
  "transcription": [
    {
      "speaker": "SPEAKER_00",
      "text": "Hello, how are you?",
      "start": 0.0,
      "end": 3.5
    },
    ...
  ]
}
```

/api/suggest-titles/ – Blog Title Suggestions
Method: POST
Payload: application/json
```json
{
  "content": "Your full blog post content goes here..."
}
```

Response:
```json
{
  "titles": [
    "How AI is Revolutionizing Content Writing",
    "Smart Tools for Smarter Blogging",
    "Leveraging NLP to Write Better Titles"
  ]
}
```
