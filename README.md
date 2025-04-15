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
git clone https://github.com/your-username/ai-django-backend.git
cd ai-django-backend
