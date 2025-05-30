import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

st.set_page_config(page_title="Video Ad Predictor", layout="centered")
st.title("🎥 GPT Video Ad Performance Predictor")

with st.form("video_form"):
    script = st.text_area("Paste your video script", height=200)
    market = st.selectbox("Market", ["UAE", "KSA", "Qatar", "Kuwait"])
    format = st.selectbox("Format", ["UGC", "Voiceover", "Demo", "Meme"])
    hook = st.selectbox("Hook", ["Text", "Pain Point", "Testimonial", "Problem-Solution"])
    submitted = st.form_submit_button("Predict")

if submitted:
    prompt = f"""
    Analyze this ad script for potential success in the {market} market.

    - Format: {format}
    - Hook Type: {hook}
    - Script: {script}

    Return:
    1. Probability of success (0–100%)
    2. One-line reasoning
    3. Two suggestions to improve it
    """

    with st.spinner("Analyzing with GPT..."):
        from openai import OpenAI

        client = OpenAI(api_key=st.secrets["openai_api_key"])

        response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
)

    result = response.choices[0].message.content

        st.markdown("### 📊 GPT Prediction Result")
        st.write(result)
