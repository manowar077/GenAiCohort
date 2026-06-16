from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
## cached input(few short prompting)
system_prompt="""
you are an ai assistent who is specilizes in maths
you should not answer any query that is not related to maths.

for a given query help user to solve that along with explanation

Ezample 1:
 input=2+2
 output:2+2is 4 which calculated by adding 2with 2
 

"""

completion=client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},#system prompt
        {"role": "user", "content": "Write a poem about the ocean."}#zero prompting   
    ]
)
print(completion.choices[0].message.content)