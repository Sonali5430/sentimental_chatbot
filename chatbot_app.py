import streamlit as st
from textblob import TextBlob

st.title("💬 Sentiment Chatbot")

# Take input from user
user_input = st.text_input("Enter your message:")

if st.button("Analyze"):
    if user_input.strip():
        analysis = TextBlob(user_input)
        polarity = analysis.sentiment.polarity

        if polarity > 0:
            st.success("😊 Sentiment:I detected your mood as Positive")
        elif polarity < 0:
            st.error("☹️ Sentiment:I detected your mood as Negative")
        else:
            st.info("😐 Sentiment:I detected your mood as Neutral")
    else:
        st.warning("⚠️ Please enter some text.")

