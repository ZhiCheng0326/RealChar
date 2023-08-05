from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset, Audio
import soundfile as sf
import torch


checkpoint = "microsoft/speecht5_tts"
processor = SpeechT5Processor.from_pretrained(checkpoint)
model = SpeechT5ForTextToSpeech.from_pretrained(checkpoint)

embeddings_dataset = load_dataset("facebook/voxpopuli", "en", split="train")
embeddings_dataset = embeddings_dataset.cast_column("audio", Audio(sampling_rate=16000))

print(embeddings_dataset[0])
# speaker_embeddings = torch.tensor(embeddings_dataset[5]["xvector"]).unsqueeze(0)

# text = """
# Greetings to all of you! 
# It is with immense pleasure and genuine warmth that I extend my heartfelt welcome to this wonderful gathering. 
# Your presence here brightens the room, and I am grateful for the opportunity to connect with such a diverse and inspiring group of individuals. 
# Whether we are old friends reuniting or new acquaintances just getting to know each other, let us embrace this moment with open hearts and open minds. 
# Together, we shall create meaningful memories, share valuable insights, and build lasting bonds. 
# So, without further ado, let's fill this space with laughter, camaraderie, and the joy of being in each other's company. 
# Hello, everyone!
# """
# inputs = processor(text=text, return_tensors="pt")

# vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
# speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

# sf.write("WiseTTS.wav", speech.numpy(), samplerate=16000)