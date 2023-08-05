import asyncio
import numpy as np
import httpx
import websockets
import sys
sys.path.append('/home/zhicheng/livenessDev/RealChar/realtime_ai_character/audio/text_to_speech/')
sys.path.append('/home/zhicheng/livenessDev/RealChar/')

from fastapi import WebSocket
from wisetts import WiseTTS

wisetts_obj = WiseTTS()
# The modified stream_audio function from before

# Your testing function
async def test_stream_audio():
    # Generate random audio data as a NumPy array (replace this with your actual audio data)
    audio_data = np.random.randint(-32768, 32767, 44100, dtype=np.int16)

    # Replace "ws://localhost:8765" with the address of your WebSocket server
    async with websockets.connect("ws://127.0.0.1:8000") as websocket:
        tts_event = asyncio.Event()
        
        TXT = 'Testing testing 1 2 3'
        
        await wisetts_obj.stream(TXT, websocket, tts_event)
        print("Audio streaming completed.")

# Run the testing function
asyncio.run(test_stream_audio())