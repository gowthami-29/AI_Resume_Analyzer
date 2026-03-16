
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from resume_parser import extract_text_from_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Cover Letter Generator", page_icon="🧾", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:800;
margin-bottom:20px;
background: linear-gradient(90deg,#ff9a9e,#fad0c4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}



.center{
display:flex;
justify-content:center;
}

.stButton button{
width:230px;
height:45px;
font-size:16px;
border-radius:10px;
font-weight:600;
background:#ff6b6b;
color:white;
}

.stButton button:hover{
background:#e63946;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">🧾 AI Cover Letter Generator</div>', unsafe_allow_html=True)

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- Input Section ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

job_title = st.text_input("💼 Job Title")

company = st.text_input("🏢 Company Name")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Generate Button ----------
st.markdown('<div class="center">', unsafe_allow_html=True)
generate = st.button("🚀 Generate Cover Letter")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Generation ----------
if generate:

    if job_title and company:

        resume_file = st.session_state.resume

        with st.spinner("Extracting resume text..."):
            resume_text = extract_text_from_pdf(resume_file)

        prompt = f"""
Write a professional cover letter for the job role '{job_title}' at '{company}'.

Use the following resume information:

{resume_text}

Keep the cover letter concise, professional, and tailored for the job.
"""

        with st.spinner("Generating cover letter..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            cover_letter = response.choices[0].message.content

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📄 Generated Cover Letter")

        st.write(cover_letter)

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("Please enter job title and company name.")

