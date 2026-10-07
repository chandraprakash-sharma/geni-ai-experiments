import os
import google.generativeai as genai

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set")

client = genai.GenerativeModel(model="gemini-2.5-flash", api_key=api_key)

def generate_text(prompt):
    response = client.generate_content(prompt)
    return response.text

print(generate_text("Hello, world!"))



