import httpx
from typing import *

class LiteFlow:
	def __init__(self, api_key: str, base_url: str = "https://liteflow.cloud"):
		self.api_key = api_key
		self.base_url = base_url

	def chat_completion(self, **kwargs):
		response = httpx.post(
			f"{self.base_url}/api/chat_completions",
			headers={"Authorization": f"Bearer {self.api_key}"},
			json=kwargs,
			timeout=30
		)
		response.raise_for_status()
		return response.text