
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from resume_parser import extract_text_from_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="ATS Resume Checker", page_icon="📑", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:800;
margin-bottom:20px;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}



.center{
display:flex;
justify-content:center;
}

.stButton button{
width:220px;
height:45px;
font-size:16px;
border-radius:10px;
font-weight:600;
background:#0072ff;
color:white;
}

.stButton button:hover{
background:#0056cc;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">📑 AI ATS Resume Checker</div>', unsafe_allow_html=True)

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- Job Description ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Paste Job Description")

job_description = st.text_area(
    "Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Button ----------
st.markdown('<div class="center">', unsafe_allow_html=True)
check = st.button("🔍 Check ATS Score")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Analysis ----------
if check:

    resume_file = st.session_state.resume

    with st.spinner("Extracting resume text..."):
        resume_text = extract_text_from_pdf(resume_file)

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

    with st.spinner("Analyzing resume for ATS compatibility..."):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 ATS Analysis Result")

    st.write(result)

    st.markdown('</div>', unsafe_allow_html=True)

