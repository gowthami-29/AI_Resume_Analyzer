
import streamlit as st
from resume_parser import extract_text_from_pdf
from jd_matcher import analyze_resume_with_jd

st.set_page_config(page_title="Resume Matcher", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:800;
margin-bottom:20px;
background: linear-gradient(90deg,#ff512f,#dd2476);
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
background:#dd2476;
color:white;
}

.stButton button:hover{
background:#b91c5c;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">💼 Resume vs Job Description Matcher</div>', unsafe_allow_html=True)

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- JD Input ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📋 Paste Job Description")

job_description = st.text_area(
    "Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Match Button ----------
st.markdown('<div class="center">', unsafe_allow_html=True)

match = st.button("🔍 Match Resume with JD")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Matching Logic ----------
if match:

    resume_file = st.session_state.resume

    with st.spinner("📄 Extracting resume text..."):
        resume_text = extract_text_from_pdf(resume_file)

    with st.spinner("🤖 Comparing Resume with Job Description..."):
        result = analyze_resume_with_jd(resume_text, job_description)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 ATS Matching Result")

    st.write(result)

    st.markdown('</div>', unsafe_allow_html=True)

