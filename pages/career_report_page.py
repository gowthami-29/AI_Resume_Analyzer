
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from resume_parser import extract_text_from_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Career Report", page_icon="📊")

st.title("📊 AI Career Report")

st.write("Get a complete career analysis based on your resume.")

# check resume
if "resume" not in st.session_state:
    st.warning("Please upload resume from dashboard first.")
    st.stop()

resume_file = st.session_state.resume
resume_text = extract_text_from_pdf(resume_file)

if st.button("Generate Career Report"):

    prompt = f"""
    Analyze the following resume and generate a career report.

    Resume:
    {resume_text}

    Provide:

    1. Resume Score out of 100
    2. Best Career Roles (3)
    3. Missing Skills
    4. Resume Improvement Suggestions
    5. Learning Roadmap
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    report = response.choices[0].message.content

    st.subheader("AI Career Report")

    st.write(report)

