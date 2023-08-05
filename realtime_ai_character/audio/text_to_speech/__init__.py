import os

from realtime_ai_character.audio.text_to_speech.base import TextToSpeech
from realtime_ai_character.logger import get_logger

logger = get_logger(__name__)

def get_text_to_speech() -> TextToSpeech:
    use = os.getenv('TEXT_TO_SPEECH_USE')

    if use == 'ELEVEN_LABS':
        from realtime_ai_character.audio.text_to_speech.elevenlabs import ElevenLabs
        ElevenLabs.initialize()
        return ElevenLabs.get_instance()
    
    elif use == 'GOOGLE_TTS':
        from realtime_ai_character.audio.text_to_speech.google_cloud_tts import GoogleCloudTTS
        GoogleCloudTTS.initialize()
        return GoogleCloudTTS.get_instance()
    
    elif use == 'WISETTS':
        from realtime_ai_character.audio.text_to_speech.wisetts import WiseTTS
        WiseTTS.initialize()
        return WiseTTS.get_instance()

    else:
        raise NotImplementedError(f'Unknown text to speech engine: {use}')
