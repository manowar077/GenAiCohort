from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
completion=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},#system prompt
        {"role": "user", "content": "Write a poem about the ocean."}#zero prompting   
    ]
)
print(completion.choices[0].message.content)