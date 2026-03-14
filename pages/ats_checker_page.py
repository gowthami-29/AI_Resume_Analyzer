import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="ATS Resume Checker", page_icon="📑")

st.title("📑 AI ATS Resume Checker")

st.write("Check if your resume passes Applicant Tracking Systems.")

resume_text = st.text_area("Paste Resume Content")

job_description = st.text_area("Paste Job Description")

if st.button("Check ATS Score"):

    if resume_text and job_description:

        prompt = f"""
        Compare the resume with the job description.

        Give:
        1. ATS Score out of 100
        2. Matched Keywords
        3. Missing Keywords
        4. Suggestions to improve resume

        Resume:
        {resume_text}

        Job Description:
        {job_description}
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        result = response.choices[0].message.content

        st.subheader("ATS Analysis")

        st.write(result)

    else:
        st.warning("Please paste both resume and job description")