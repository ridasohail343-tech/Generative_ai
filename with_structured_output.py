from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Literal,Optional
from pydantic import BaseModel
load_dotenv()

model=ChatOpenAI()
class Revision(BaseModel):
    name:Annotated[str,"write down your name"]
    age:Annotated[int,"write down your age"]

model_structure_output=model.with_structured_output(Revision)


result=model_structure_output.invoke(""" Hardware refers to the physical components of a computer, such as the CPU, RAM, keyboard, and monitor. It includes all the tangible parts of a computer system that can be seen and touched.""")