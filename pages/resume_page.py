import streamlit as st
import os
import re
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume
from groq import Groq
from db import save_resume

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

# ---------- PROTECT PAGE ----------
if "user" not in st.session_state:
    st.warning("⚠ Please login first")
    st.switch_page("pages/login_page.py")

# ---------- TITLE ----------
st.markdown('<div class="title">📄 AI Resume Analyzer</div>', unsafe_allow_html=True)

# ---------- CHECK RESUME ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- BUTTONS ----------
col1, col2 = st.columns(2)

with col1:
    analyze = st.button("🚀 Analyze Resume")

with col2:
    improve = st.button("✨ Improve Resume")

# ---------- EXTRACT TEXT ----------
resume_file = st.session_state.resume
resume_text = extract_text_from_pdf(resume_file)

# ---------- IMPROVE ----------
if improve:

    prompt = f"""
    Improve the following resume content and make it professional.

    Resume:
    {resume_text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    improved_resume = response.choices[0].message.content

    st.subheader("✨ Improved Resume")
    st.write(improved_resume)

# ---------- ANALYZE ----------
if analyze:

    with st.spinner("🤖 AI analyzing your resume..."):
        result = analyze_resume(resume_text)

    st.subheader("📊 Resume Analysis Result")
    st.write(result)

    # ---------- SCORE EXTRACTION (SAFE) ----------
    match = re.search(r"Score:\s*(\d+)", result)

    if match:
        score = int(match.group(1))
    else:
        # fallback (if AI format is wrong)
        numbers = re.findall(r"\d+", result)
        score = int(numbers[-1]) if numbers else 0

    # ---------- SAVE ----------
    save_resume(
        st.session_state.user["id"],
        resume_text[:100],
        score
    )

    # ---------- DEBUG ----------
    st.write("Extracted score:", score)

    st.success(f"✅ Saved! Score: {score}")