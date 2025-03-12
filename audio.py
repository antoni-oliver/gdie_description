# https://huggingface.co/microsoft/speecht5_tts
# pip install datasets soundfile sentencepiece

import json
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch
synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts") #TODO és per fer audios en anglès

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

text = json.loads(open("audio_es.json", "r").read())

ffmpeg = "ffmpeg "

for i in range(len(text)):
    chunk = text[i]
    offset = chunk["timestamp"][0]
    print(chunk["text"])
    speech = synthesiser(chunk["text"], forward_params={"speaker_embeddings": speaker_embedding})
    sf.write(f"audio/audio_es_{i}.wav", speech["audio"], samplerate=speech["sampling_rate"])
    ffmpeg += f"-itsoffset {offset} -i audio/audio_es_{i}.wav " #TODO faltaria retallar els trossos més grossos que la mida del chunk

ffmpeg += f"-filter_complex amix=inputs={i+1} -async 1 -c:a aac audio_es.m4a"
print(ffmpeg)