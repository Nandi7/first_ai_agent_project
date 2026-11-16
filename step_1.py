import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    timeout=60,
)

# generating a response (LLM)
response = client.chat.completions.create(
    model="models/gemini-2.5-flash",
    messages=[  # the prompt, what we are passing to the LLM
        {
            "role": "system",
            "content": "You are a helpful AI assistant. Answer in short messages.",
        },
        {
            "role": "user",
            "content": "Explain what an AI agent is in one sentence.",
        },
    ],
)

# taking the response and printing it out
print(response.choices[0].message.content)