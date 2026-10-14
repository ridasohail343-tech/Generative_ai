from langchain_core.prompts import PromptTemplate
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
template.save('template.json')