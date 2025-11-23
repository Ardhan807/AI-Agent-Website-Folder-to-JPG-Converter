import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_ai(messages, model="x-ai/grok-4.1-fast"):
    if not OPENROUTER_API_KEY:
        return "[ERROR] API key tidak ditemukan."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",
        "X-Title": "HTML PDF Agent",
    }

    try:
        response = requests.post(
            OPENROUTER_URL,
            json={"model": model, "messages": messages},
            headers=headers,
            timeout=30
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "[ERROR] Request timeout, coba lagi."
    except Exception as e:
        return f"[ERROR] API gagal: {e}"
