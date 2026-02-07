import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
API_PORT = int(os.getenv("API_PORT", 8000))
API_HOST = os.getenv("API_HOST", "0.0.0.0")

# Modelos disponíveis
MODEL_DEFAULT = "gpt-3.5-turbo"
TEMPERATURE = 0.7
MAX_TOKENS = 1024
