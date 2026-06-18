from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()

response=client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "what is the weather in Dhanbad jharkhand today?"}
    ]
)
print(response.choices[0].message.content)