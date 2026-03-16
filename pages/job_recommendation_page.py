
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from resume_parser import extract_text_from_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Career Recommendation", page_icon="🚀", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:800;
margin-bottom:20px;
background: linear-gradient(90deg,#43e97b,#38f9d7);
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
background:#00a86b;
color:white;
}

.stButton button:hover{
background:#007f5f;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">🚀 AI Career Role Recommendation</div>', unsafe_allow_html=True)

st.write("Get career role suggestions based on your resume.")

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- Button ----------
st.markdown('<div class="center">', unsafe_allow_html=True)
recommend = st.button("🔎 Recommend Career Roles")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Recommendation ----------
if recommend:

    resume_file = st.session_state.resume

    with st.spinner("Extracting resume text..."):
        resume_text = extract_text_from_pdf(resume_file)

    prompt = f"""
Based on the following resume, suggest 5 suitable career roles.

Resume:
{resume_text}

Also provide a short reason for each role.
"""

    with st.spinner("Analyzing resume and generating career suggestions..."):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🎯 Recommended Career Roles")

    st.write(result)

    st.markdown('</div>', unsafe_allow_html=True)
