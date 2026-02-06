from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

llm_prompt = """
                I am a medical assistant
                Rules: 
                1. Provide only general healthcare and medical information 
                2. Do not diagnose the disease
                3. Do not prescribe or recommend medications and dosages
                4. Always recommend consulting a doctor
             """

prompt = ChatPromptTemplate.from_messages([("system",llm_prompt),("human","{input_parameters}")])
llm =  OllamaLLM(model="llama3", temperature=0.5)

chain = prompt | llm