import os
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


_client: Optional[OpenAI] = None


def _get_client() -> Optional[OpenAI]:
  global _client
  if _client is not None:
    return _client
  api_key = os.getenv("OPENAI_API_KEY")
  if api_key:
    _client = OpenAI(api_key=api_key)
    return _client
  return None


def generate_text(prompt: str) -> str:
  """Generate text using the OpenAI client if configured.

  If `OPENAI_API_KEY` is not set, returns a mocked response so the app
  can run without failing during development.
  """
  client = _get_client()
  if client is None:
    return f"[MOCKED RESPONSE] You sent: {prompt}"

  resp = client.responses.create(model="gpt-4.1-mini", input=prompt)
  # Best-effort: try to return the expected text field
  if hasattr(resp, "output_text"):
    return resp.output_text
  # Fallback to string representation
  return str(resp)


