from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)
model=ChatHuggingFace(llm=llm)

response=model.invoke("What is the capital of France ?")
print(response.content)