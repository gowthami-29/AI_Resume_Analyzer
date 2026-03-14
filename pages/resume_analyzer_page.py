import streamlit as st
from PyPDF2 import PdfReader
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("📄 AI Resume Analyzer")

# Upload PDF
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])


# Function to extract text
def extract_text_from_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text


if uploaded_file:

    resume_text = extract_text_from_pdf(uploaded_file)

    st.subheader("Extracted Resume Text")
    st.write(resume_text[:500])  # preview first 500 chars


    if st.button("Analyze Resume"):

        prompt = f"""
        Analyze this resume and provide:

        1. Resume summary
        2. Key skills
        3. Strengths
        4. Improvements

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

        st.subheader("AI Analysis")

        st.write(result)

        # Download result
        st.download_button(
            "Download Result",
            data=result,
            file_name="resume_analysis.txt"
        )