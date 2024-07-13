import streamlit as st
import langchain
import os
from langchain_google_genai import ChatGoogleGenerativeAI as CGGA
os.environ["GOOGLE_API_KEY"]  = st.secrets["OPEN_API_KEY"]

st.title("Tweet Generator")
st.subheader("Generate Tweets on any topic")
topic = st.text_input("Topic")
number = st.number_input("No. of tweets",min_value=1,max_value=10,step=1,value=1)
gemini_model = CGGA(model="gemini-1.5-flash-latest")

if st.button("Generate"):
    st.write(topic)
    st.write(number)
    prompt = f"Give me {number} of tweets on {topic}"
    response=gemini_model.invoke(prompt)
    st.write(response.content)
