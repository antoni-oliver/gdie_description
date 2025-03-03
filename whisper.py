from transformers import pipeline
transcriber = pipeline(model="openai/whisper-large-v2", torch_dtype="auto")
print(transcriber('audio2.m4a', return_timestamps=True, generate_kwargs={"language": "english"}))