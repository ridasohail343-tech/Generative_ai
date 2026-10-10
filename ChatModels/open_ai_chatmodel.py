from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm=ChatOpenAI(
     model="gpt-4o-mini",
    temperature=0.7
)
result=llm.invoke('who is the primeminister of india')
print(result.content)