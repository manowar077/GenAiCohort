from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)
while True:
    prompt=input("Enter your question: ")
    if prompt=="0":
        break
    response = llm.invoke(prompt)

    print("Bot :hello",response.content)