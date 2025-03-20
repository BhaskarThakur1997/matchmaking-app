import streamlit as st
import requests
import random

st.set_page_config(page_title="MatchAI", layout="centered")

st.title("💖 MatchAI - AI-Powered Matchmaking")

user_name = st.text_input("Enter your name:")

if st.button("Find Matches"):
    response = requests.get("http://127.0.0.1:5000/get_matches")
    if response.status_code == 200:
        matches = response.json()
        st.write(f"Hey {user_name}! Here are your best matches:")
        
        for match in matches:
            st.image(match["image"], width=100)
            st.subheader(match["name"])
            st.write(f"🔥 Compatibility: {match['compatibility']}")
            st.write(f"🎉 Event: {match['event']}")
            st.divider()
    else:
        st.error("Error fetching matches. Try again!")

st.subheader("💬 AI Chat")
message = st.text_input("Type your message:")

bot_responses = [
    "Tell me more about yourself!",
    "What are your hobbies?",
    "Would you rather go to a concert or a tech meetup?",
    "How do you like meeting new people?",
    "What's your favorite way to start a conversation?"
]

if st.button("Send"):
    st.write(f"💬 You: {message}")
    st.write(f"🤖 AI: {random.choice(bot_responses)}")
