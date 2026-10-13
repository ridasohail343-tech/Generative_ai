from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()

model=ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

st.header("research tool")

# paper_input
paper_input=st.selectbox("select the research_paper name",[  "Attention Is All You Need",
    "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",
    "A Survey on Large Language Models"])

# explanation style
explaination_style=st.selectbox("select your explaination style",['basic','intermediate','advanced'])

# length
length=st.selectbox("select the length",["short","medium","detailed"])


# template
template=PromptTemplate(
  template="""
summarize the research_paper titled {paper_input} with the following specifications :
explaination style should be{explaination_style} length of the paper should be {length}

    Include the following:
    1. Main objective
    2. Methodology
    3. Key findings
    4. Conclusion

    Write the summary in simple and clear language.
""",
input_variables=['paper_input','explaination_style','length'],
validate_template=True
)
prompt=template.invoke({
    "paper_input":paper_input,
    "explaination_style":explaination_style,
    "length":length 

})

if st.button('summarize'):
    result=model.invoke(prompt)
    st.write(result.content)
