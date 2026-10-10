from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
import os
load_dotenv()
token=os.getenv('HUGGING_FACE_API_KEY')
llm=HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-1.5B-Instruct",
    task="text-generation",
    max_new_tokens=1000,
    huggingfacehub_api_token=token
)

model=ChatHuggingFace(llm=llm)
result=model.invoke('what is the capital of india')
print(result)