from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
#generating a response (LLM)
response = client.chat.completions.create(
    model= "gpt-5-mini",
    messages= [ #the promt, what we are passing to the LLM
        {"role": "system", "content": "You are a helpful AI assistant. Answer in short messages."},
        {"role": "user", "content": "Explain what an AI agent is in one sentence."},
        {"role": "assistant", "content": "An AI agent is an LLM connected to a loop."}
    ],
)
#taking the response and printing it out
print(response.choices[0].message.content)