from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding_model=OpenAIEmbeddings(
       model="text-embedding-3-small"
)
result=embedding_model.embed_query("what is capital of  japan")
print(result)
