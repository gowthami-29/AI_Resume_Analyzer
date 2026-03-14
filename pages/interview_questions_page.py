import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

st.set_page_config(page_title="Interview Question Generator", page_icon="🎤")

st.title("🎤 AI Interview Question Generator")

st.write("Generate interview questions based on your resume")

resume_text = st.text_area("Paste Resume Content")

if st.button("Generate Questions"):

    if resume_text:

        prompt = f"""
        Based on the following resume, generate 5 technical interview questions.

        Resume:
        {resume_text}
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        questions = response.choices[0].message.content

        st.subheader("Generated Interview Questions")

        st.write(questions)

    else:
        st.warning("Please paste your resume")