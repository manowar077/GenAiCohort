from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

load_dotenv()
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
# Verify API key is loaded
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

try:
    model = ChatGroq(model_name="llama-3.1-8b-instant", api_key=api_key)
    response = model.invoke("what is Gross Domestic product !")
    print(response.content)
except Exception as e:
    print(f"Error: {e}")