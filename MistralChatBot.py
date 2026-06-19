from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)
messages=[]
while True:
    prompt=input("Enter your question: ")
    messages.append(prompt)
    if prompt=="0":
        break
    response = llm.invoke(messages)
    messages.append(response.content)

    print("Bot :hello",response.content) 