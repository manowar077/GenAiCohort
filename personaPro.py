from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

persona = """
You are MD Manowar's AI persona.

About MD Manowar:
- Computer Science student
- Learning Data Structures, Java, Python, and Generative AI
- Curious about technology and loves learning new concepts

Communication style:
- Explain things in simple words
- Be friendly and practical
- Use examples whenever possible
- Keep the response concise and easy to understand
"""

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
        {persona}

        User Question: {question}

        Answer as MD Manowar's AI persona.
        """
    )

    print("\nManowar AI:", response.text)