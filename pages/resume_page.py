
import streamlit as st
import os
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:42px;
font-weight:800;
margin-bottom:20px;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}



.center{
display:flex;
justify-content:center;
margin-top:15px;
}

.stButton button{
width:200px;
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
st.markdown('<div class="title">📄 AI Resume Analyzer</div>', unsafe_allow_html=True)

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

# ---------- Resume Loaded Card ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.success("✅ Resume loaded successfully")

st.write("Your uploaded resume is ready for AI analysis.")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Analyze Button ----------
st.markdown('<div class="center">', unsafe_allow_html=True)

analyze = st.button("🚀 Analyze Resume")

st.markdown('</div>', unsafe_allow_html=True)
resume_file = st.session_state.resume
resume_text = extract_text_from_pdf(resume_file)
if st.button("Improve Resume"):
    

    prompt = f"""
    Improve the following resume content and make it professional.

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role":"user","content":prompt}]
    )

    improved_resume = response.choices[0].message.content

    st.subheader("Improved Resume")
    st.write(improved_resume)

# ---------- Analysis ----------
if analyze:

    resume_file = st.session_state.resume

    with st.spinner("🔎 Extracting resume text..."):
        resume_text = extract_text_from_pdf(resume_file)

    with st.spinner("🤖 AI analyzing your resume..."):
        result = analyze_resume(resume_text)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Resume Analysis Result")

    st.write(result)

    st.markdown('</div>', unsafe_allow_html=True)

