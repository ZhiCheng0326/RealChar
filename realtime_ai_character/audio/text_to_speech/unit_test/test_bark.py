from transformers import AutoProcessor, BarkModel
import scipy

processor = AutoProcessor.from_pretrained("suno/bark")
model = BarkModel.from_pretrained("suno/bark")

voice_preset = "v2/en_speaker_6"

text = """
Greetings to all of you! 
It is with immense pleasure and genuine warmth that I extend my heartfelt welcome to this wonderful gathering. 
Your presence here brightens the room, and I am grateful for the opportunity to connect with such a diverse and inspiring group of individuals. 
Whether we are old friends reuniting or new acquaintances just getting to know each other, let us embrace this moment with open hearts and open minds. 
Together, we shall create meaningful memories, share valuable insights, and build lasting bonds. 
So, without further ado, let's fill this space with laughter, camaraderie, and the joy of being in each other's company. 
Hello, everyone!
"""

inputs = processor(text, voice_preset=voice_preset)

audio_array = model.generate(**inputs)
audio_array = audio_array.cpu().numpy().squeeze()

sample_rate = model.generation_config.sample_rate


sample_rate = model.generation_config.sample_rate
scipy.io.wavfile.write("bark_out.wav", rate=sample_rate, data=audio_array)
