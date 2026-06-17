from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are a helpful AI assistant specialized in character analysis.
Provide thoughtful and detailed responses.
"""

user_query = input("Enter your question: ")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
)
print(completion.choices[0].message.content)