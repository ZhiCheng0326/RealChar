from TTS.api import TTS
import numpy as np

print(TTS.list_models())

# model_name = 'tts_models/multilingual/multi-dataset/your_tts'
# model_name = 'tts_models/en/ljspeech/glow-tts'
# model_name = "tts_models/multilingual/multi-dataset/bark"
model_name = 'tts_models/en/vctk/vits' #good
tts = TTS(model_name)

print(f"Number of speakers: {len(tts.speakers)}")
text = """
Greetings to all of you! 
It is with immense pleasure and genuine warmth that I extend my heartfelt welcome to this wonderful gathering. 
Your presence here brightens the room, and I am grateful for the opportunity to connect with such a diverse and inspiring group of individuals. 
Whether we are old friends reuniting or new acquaintances just getting to know each other, let us embrace this moment with open hearts and open minds. 
Together, we shall create meaningful memories, share valuable insights, and build lasting bonds. 
So, without further ado, let's fill this space with laughter, camaraderie, and the joy of being in each other's company. 
Hello, everyone!
"""

# ##### USE SPEAKER 6 ##### 
# for idx, spkr in enumerate(tts.speakers):
#     # tts.tts_to_file(text=text, speaker=spkr, file_path=f"vits_{idx}.wav") # vits, fast_pitch
#     wav = tts.tts(text=text, speaker=spkr) # wav is list
#     # if idx == 10:
#     #     break

# tts.tts_to_file(text=text, file_path="coquitts.wav")
tts.tts_to_file(text=text, speaker=tts.speakers[6], file_path="coquitts.wav") # vits, fast_pitch
# tts.tts_to_file(text=text, speaker=tts.speakers[1], language=tts.languages[0], file_path="coquitts.wav") # your_tts

