
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from resume_parser import extract_text_from_pdf

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

st.set_page_config(page_title="Interview Question Generator", page_icon="🎤", layout="centered")

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
width:230px;
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
st.markdown('<div class="title">🎤 AI Interview Question Generator</div>', unsafe_allow_html=True)

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- Generate Questions ----------
st.markdown('<div class="center">', unsafe_allow_html=True)
generate = st.button("🚀 Generate Interview Questions")
st.markdown('</div>', unsafe_allow_html=True)

if generate:

    resume_file = st.session_state.resume

    with st.spinner("Extracting resume text..."):
        resume_text = extract_text_from_pdf(resume_file)

    prompt = f"""
    Based on the following resume, generate 5 technical interview questions.

    Resume:
    {resume_text}
    """

    with st.spinner("Generating interview questions using AI..."):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        questions = response.choices[0].message.content

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📋 Generated Interview Questions")

    st.write(questions)

    st.markdown('</div>', unsafe_allow_html=True)

