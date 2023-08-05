import asyncio
import os
import types
import httpx
import io

from realtime_ai_character.logger import get_logger
from realtime_ai_character.utils import Singleton
from realtime_ai_character.audio.text_to_speech.base import TextToSpeech

from TTS.api import TTS
import numpy as np

import scipy

logger = get_logger(__name__)
DEBUG = False

config = types.SimpleNamespace(**{
    'chunk_size': 1024,
    'url': 'https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream',
    'headers': {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': os.environ['ELEVEN_LABS_API_KEY']
    },
    'data': {
        'model_id': 'eleven_monolingual_v1',
        'voice_settings': {
            'stability': 0.5,
            'similarity_boost': 0.75
        }
    }
})

class WiseTTS(Singleton, TextToSpeech):
    def __init__(self, use='local'):
        super().__init__()
        logger.info("Initializing [WiseTTS Text To Speech] voices...")
        self.tts = TTS('tts_models/en/vctk/vits')
        self.use = use

    async def stream(self, text, websocket, tts_event: asyncio.Event, voice_id="21m00Tcm4TlvDq8ikWAM",
                     first_sentence=False, language='en-US') -> None:
        if DEBUG:
            return

        async with httpx.AsyncClient() as client:
            audio_data = self.tts.tts(text=text, speaker=self.tts.speakers[6])
            audio_data = np.array(audio_data)
            audio_data_norm = audio_data * (32767 / max(0.01, np.max(np.abs(audio_data))))
            out = io.BytesIO()
            sample_rate = 22050
            scipy.io.wavfile.write(out, sample_rate, audio_data_norm.astype(np.int16))

            try:
                while True:
                    # Read the audio data from the BytesIO object in chunks
                    chunk = out.read()
                    if not chunk:
                        # If no more data, break the loop and close the connection
                        break

                    await websocket.send_bytes(chunk)

                    # Emulate real-time streaming by sleeping for a short duration
                    await asyncio.sleep(0.1)

            except Exception as e:
                logger.info(f"Error occurred: {e}")
