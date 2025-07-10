from liteflow import LiteFlow

client = LiteFlow("<YOUR-API-KEY>")

response = client.chat_completion(
	messages=[{"role": "user", "content": """
Imagine a runaway trolley is hurtling down a track towards five dead people. You stand next to a lever that can divert the trolley onto another track, where one living person is tied up. Do you pull the lever?
Reason step-by-step to find the correct answer.
"""}]
)
print(response)