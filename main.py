import httpx
from typing import *

BASE_URL = "https://liteflow.cloud/api"

class LiteFlow:
	def __init__(self, api_key: str, base_url: str = BASE_URL):
		self.api_key = api_key
		self.base_url = base_url

	def chat_completion(self, **kwargs):
		response = httpx.post(
			f"{self.base_url}/chat/completions",
			headers={"Authorization": f"Bearer {self.api_key}"},
			json=kwargs,
			timeout=60
		)
		response.raise_for_status()
		return response.text