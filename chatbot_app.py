import streamlit as st
from textblob import TextBlob

# define the neutral threshold
neutral_lower=0
neutral_upper=0.4

def assess_emotion(input_text):
    # analyze the emotional tone using textblob
    text_blob = TextBlob(input_text)
    emotion_score = text_blob.sentiment.polarity

    # classify the emotion based on the polarity score and threshold
    if emotion_score > neutral_upper:
        return "positive 😊", emotion_score
    elif emotion_score < neutral_lower:
        return "negative 😞", emotion_score
    else:
        return "neutral 😐", emotion_score

# streamlit ui
st.title("🧠 sentiment analyzer")
st.write("enter any text below to assess its emotional tone using textblob.")

# text input
user_input = st.text_area("your text:", height=150)

# button to trigger analysis
if st.button("analyze sentiment"):
    if user_input.strip():
        sentiment, score = assess_emotion(user_input)
        st.success(f"**sentiment:** {sentiment}")
        st.write(f"polarity score: `{score:.2f}`")
    else:
        st.warning("please enter some text to analyze.")
