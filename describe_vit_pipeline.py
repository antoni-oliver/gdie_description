from transformers import pipeline

image_to_text = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")

for i in range(63):
    image = f"thumb_{i+1}.jpg"
    start = i * 10
    end = (i + 1) * 10
    desc = image_to_text(image)
    desc = desc[0]['generated_text']
    print(f"{start} --> {end}\n{desc}")