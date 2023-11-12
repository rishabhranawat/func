import json
import time
import os

import requests
import openai
from lib import functions

openai.api_key = os.getenv('OPENAI_API_KEY')
GPT_MODEL = "gpt-3.5-turbo"

def chat_completion_request(messages, functions=None, function_call=None, model=GPT_MODEL):
	headers = {
		"Content-Type": "application/json",
		"Authorization": "Bearer " + openai.api_key,
	}
	json_data = {"model": model, "messages": messages}
	if functions is not None:
		json_data.update({"functions": functions})
	if function_call is not None:
		json_data.update({"function_call": function_call})
	try:
		response = requests.post(
			"https://api.openai.com/v1/chat/completions",
			headers=headers,
			json=json_data,
		)
		return response
	except Exception as e:
		print("Unable to generate ChatCompletion response")
		print(f"Exception: {e}")
		return e

messages = []

messages.append({"role": "system", \
	"content": "Don't make assumptions about what values to plug into functions. \
	Ask for clarification if a user request is ambiguous."})

messages.append({"role": "user", \
	"content": "What's the weather like today in Glasgow"})

chat_response = chat_completion_request(
	messages, functions=functions()
)
assistant_message = chat_response.json()["choices"][0]["message"]
messages.append(assistant_message)
print(assistant_message)

