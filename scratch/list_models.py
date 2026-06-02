import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
for model in client.models.list():
    if 'generateContent' in getattr(model, 'supported_actions', []):
        print(f"Name: {model.name} -> {model.display_name}")
