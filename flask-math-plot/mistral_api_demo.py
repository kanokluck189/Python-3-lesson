import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")

if not API_KEY:
    raise RuntimeError("MISTRAL_API_KEY not found in .env")

#GET USER INPUT FROM TERMINAL
user_request = input("Describe the function to plot: ")

url = "https://api.mistral.ai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

prompt = (
    "Convert the following request into a valid Python mathematical "
    "expression using variable x.\n"
    "Return ONLY the expression.\n\n"
    f"Request: {user_request}"
)

data = {
    "model": "mistral-small",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "temperature": 0
}

response = requests.post(url, headers=headers, json=data)

print("\nLLM output:")
print(response.json()["choices"][0]["message"]["content"])
