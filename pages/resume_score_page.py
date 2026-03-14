import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Resume Score Analyzer", page_icon="📊")

st.title("📊 AI Resume Score Analyzer")

st.write("Upload or paste your resume to get a score and improvement suggestions.")

resume_text = st.text_area("Paste Resume Content")

if st.button("Analyze Resume"):

    if resume_text:

        prompt = f"""
        Analyze the following resume and give:

        1. Resume Score out of 100
        2. Strengths
        3. Improvements

        Resume:
        {resume_text}
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        result = response.choices[0].message.content

        st.subheader("Analysis Result")

        st.write(result)

    else:
        st.warning("Please paste your resume")