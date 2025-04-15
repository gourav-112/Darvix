import os
import tempfile
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
from django.views import View
import json

# For audio transcription and diarization
import torch
from transformers import pipeline

# For blog title generation
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load transcription and diarization pipeline (using Whisper with speaker diarization capabilities)
# Note: Pyannote-audio or WhisperX is often used for diarization; here's a simple mock approach.
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-large")

title_model = T5ForConditionalGeneration.from_pretrained("t5-base")
title_tokenizer = T5Tokenizer.from_pretrained("t5-base")

@method_decorator(csrf_exempt, name='dispatch')
class AudioTranscriptionView(View):
    def post(self, request):
        audio_file = request.FILES.get("audio")
        if not audio_file:
            return JsonResponse({"error": "No audio file provided."}, status=400)

        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp:
            for chunk in audio_file.chunks():
                tmp.write(chunk)
            tmp_path = tmp.name

        try:
            result = transcriber(tmp_path)
            transcription_text = result["text"]

            # Mock diarization for demonstration
            diarized_result = {
                "speakers": [
                    {"speaker": "Speaker 1", "text": transcription_text[:len(transcription_text)//2]},
                    {"speaker": "Speaker 2", "text": transcription_text[len(transcription_text)//2:]},
                ]
            }

            return JsonResponse({
                "transcription": transcription_text,
                "diarization": diarized_result
            })
        finally:
            os.remove(tmp_path)


@method_decorator(csrf_exempt, name='dispatch')
class TitleSuggestionView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            content = data.get("content", "")
            if not content:
                return JsonResponse({"error": "No content provided."}, status=400)

            input_text = f"generate blog titles: {content}"
            input_ids = title_tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

            outputs = title_model.generate(input_ids, max_length=64, num_return_sequences=3, do_sample=True)
            titles = [title_tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

            return JsonResponse({"suggested_titles": titles})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON."}, status=400)


