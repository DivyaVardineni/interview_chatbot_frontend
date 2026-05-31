import streamlit as st
import requests


server_loc=""

st.title(" AI Interview learninig Chatbot")


language=st.text_input("enter language")
topic=st.text_input("enter Topic ")
difficulty=st.selectbox("select difficulty",["easy","medium","hard"])

learning_mode=st.selectbox("select learning mode",["MCQS","theory Questions","Code snipppets"])

if st.button("Generate"):
    prompt=f"""
    Generate interview preparation content.

    Language: {language}
    Topic: {topic}
    Difficulty: {difficulty}
    Learning Mode: {learning_mode}
    """

    data={
        "prompt":prompt
    }
    res=requests.post(f"{server_loc}/questions",json=data)
   
    st.write(res.json()["response"])