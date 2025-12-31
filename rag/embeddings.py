from openai import OpenAI
import os

def get_client():
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def embed_text(text: str):
    # vetor fake só para fluxo funcionar
    return [0.1] * 384

