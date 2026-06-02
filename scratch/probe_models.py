import os
from google import genai
from google.genai.errors import APIError
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
test_models = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-pro",
    "gemini-3.5-flash",
    "gemini-3.1-flash-lite",
    "gemini-2.0-flash-lite",
]

for model_name in test_models:
    try:
        response = client.models.generate_content(
            model=model_name,
            contents="Say hi",
        )
        print(f"✅ Model {model_name} is WORKING! Response: {response.text.strip()}")
    except APIError as e:
        print(f"❌ Model {model_name} FAILED: {e.message}")
    except Exception as e:
        print(f"❌ Model {model_name} ERROR: {e}")
