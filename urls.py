import os
from django.urls import path
from .views import AudioTranscriptionView, TitleSuggestionView

urlpatterns = [
    path("api/transcribe/", AudioTranscriptionView.as_view(), name="audio-transcription"),
    path("api/suggest-titles/", TitleSuggestionView.as_view(), name="title-suggestions"),
]


# settings.py (Ensure the following are installed and configured)
# pip install transformers torch librosa
# MEDIA settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Add to installed apps if needed
# INSTALLED_APPS = [..., 'django.contrib.staticfiles']
