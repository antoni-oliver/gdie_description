import time

start = time.time()
from transformers import pipeline
transcriber = pipeline(model="openai/whisper-tiny", torch_dtype="auto")
print(transcriber('audio2.m4a', return_timestamps=True, generate_kwargs={"language": "english"}))
end = time.time()
print(end - start)