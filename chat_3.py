from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

system_prompt = """You are an AI assistant who specializes in breaking down complex problems into simple explanations.
For the given query, help the user to solve it along with a detailed explanation. Break it down into step-by-step solutions.
Think through at least 5-6 steps to solve the problem before providing the final answer.

Analyze the user input carefully and return output in structured format.

Example 1:
Input: What is the sum of 2+2?
Output: 
Step 1 (Analyze): The user is asking for a basic arithmetic operation - addition.
Step 2 (Think): To perform addition, we add 2 with 2.
Step 3 (Calculate): 2 + 2 = 4
Step 4 (Verify): Check: 2 + 2 = 4 ✓
Step 5 (Explain): The sum of 2 and 2 is 4.
"""

user_query = input("Enter your question: ")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"{system_prompt}\n\nUser Query: {user_query}"
)

print(response.text)