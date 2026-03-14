import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Cover Letter Generator", page_icon="🧾")

st.title("🧾 AI Cover Letter Generator")

st.write("Generate a professional cover letter using your resume.")

job_title = st.text_input("Job Title")

company = st.text_input("Company Name")

resume_text = st.text_area("Paste Resume Content")

if st.button("Generate Cover Letter"):

    if job_title and company and resume_text:

        prompt = f"""
        Write a professional cover letter for the job role
        '{job_title}' at '{company}'.

        Use the following resume information:

        {resume_text}

        Keep the cover letter concise and professional.
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        cover_letter = response.choices[0].message.content

        st.subheader("Generated Cover Letter")

        st.write(cover_letter)

    else:
        st.warning("Please fill all fields")