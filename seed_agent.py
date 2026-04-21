import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. We plug in the Gemini Brain using your VIP card
agent_brain = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key="AIzaSyB46f-lTTyy1sAxPFIhFIDzjRIJqpuVWRY")

# 2. We give the robot a friendly face and a chat box
st.title("🌱 S.E.E.D Clinical Co-Pilot")
user_message = st.chat_input("Type a message to your S.E.E.D Agent...")

# 3. We tell it to answer when a parent types a message
if user_message:
    st.chat_message("user").write(user_message)          # Shows what you typed
    answer = agent_brain.invoke(user_message)            # The brain thinks about it
    st.chat_message("assistant").write(answer.content)   # The robot replies!