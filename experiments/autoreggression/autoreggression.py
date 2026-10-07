from transformers import pipeline
generator = pipeline("text-generation", model="distilgpt2")

prompt = "The future of AI is"

result = generator(prompt, max_length=20)

print(result[0]['generated_text'])