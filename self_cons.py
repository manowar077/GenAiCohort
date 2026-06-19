#self - Consistency prompting
#its method is to generate multiple outputs possible  for the same input and then select 
#the most consistent answer among them. This approach can help improve the reliability of the model's responses by leveraging the consensus among multiple outputs.
from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_with_retry(question, max_retries=3, wait_time=2):
    """Generate content with automatic retry logic for server errors"""
    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Answer this question in a different way: {question}"
            )
            return response.text
        except genai.errors.ClientError as e:
            # Handle quota/rate limit errors (429)
            if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
                if attempt < max_retries - 1:
                    print(f"\n⏳ Quota limit hit (attempt {attempt + 1}/{max_retries}). Waiting {wait_time * 3}s before retry...")
                    time.sleep(wait_time * 3)  # Wait longer for quota errors
                else:
                    raise e
            else:
                raise e
        except genai.errors.ServerError as e:
            if attempt < max_retries - 1:
                print(f"\n⏳ Server busy (attempt {attempt + 1}/{max_retries}). Waiting {wait_time}s before retry...")
                time.sleep(wait_time)
            else:
                raise e


while True:
    question = input("You: ")

    if question == "exit":
        break

    answers = []

    # Generate 5 answers
    for i in range(5):
        try:
            answer = generate_with_retry(question)
            answers.append(answer)
            print(f"  ✓ Answer {i+1} generated")
        except genai.errors.ServerError as e:
            print(f"  ✗ Failed after retries: {e}")
            break

    if len(answers) < 5:
        print("Could not generate enough answers. Please try again later.\n")
        continue

    # Ask AI to choose the best answer
    try:
        formatted_answers = "\n".join([f"{i+1}. {ans}" for i, ans in enumerate(answers)])
        
        final = generate_with_retry(
            f"""I have 5 answers for the question '{question}':

{formatted_answers}

Choose the most accurate and clear answer.
Return only the final answer."""
        )

        print("\nBot:", final)
    except genai.errors.ServerError as e:
        print(f"Failed to select best answer: {e}\n")

