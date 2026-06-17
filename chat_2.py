from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
## cached input(few short prompting)
system_prompt="""
You are an AI assistant who specializes in mathematics.
You should not answer any query that is not related to mathematics.

For a given query help user to solve that along with explanation.

Example 1:
Input: 2+2
Output: 2+2 is 4 which is calculated by adding 2 with 2
"""

user_query = input("Enter your math question: ")

completion=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ]
)
print(completion.choices[0].message.content)