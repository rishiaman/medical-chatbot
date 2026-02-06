import streamlit as st
import requests

st.title("Medical Information Chatbot")
st.warning("This Bot provides only General Medical information and not consultation or advice")

API_URL = "http://localhost:8000/medical_chat/invoke"

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask me any health related queries")
if user_input: 
    st.session_state.messages.append({"roles":"user", "content":user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    payload = {"input":user_input}
    response = requests.post(API_URL, json=payload).json()
    
   # bot_reponse = response["output"]
    st.session_state.messages.append({"roles":"assistant", "content":response})
    with st.chat_message("assistant"):
        st.markdown(response)
