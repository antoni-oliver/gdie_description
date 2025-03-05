import time

start = time.time()
from transformers import pipeline
transcriber = pipeline(model="openai/whisper-tiny", torch_dtype="auto", chunk_length_s=10)
print(transcriber('audio2.m4a', batch_size=8, return_timestamps=True))
end = time.time()
print(end - start)