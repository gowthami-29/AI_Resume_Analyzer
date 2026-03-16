
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from resume_parser import extract_text_from_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Learning Roadmap", page_icon="📚", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:800;
margin-bottom:20px;
background: linear-gradient(90deg,#f6d365,#fda085);
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
background:#f97316;
color:white;
}

.stButton button:hover{
background:#ea580c;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">📚 AI Learning Roadmap Generator</div>', unsafe_allow_html=True)

st.write("Generate a personalized learning roadmap based on your resume and career goal.")

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- Input Section ----------
st.markdown('<div class="card">', unsafe_allow_html=True)

career_goal = st.text_input(
    "🎯 Target Job Role",
    placeholder="Example: Data Scientist, Backend Developer, AI Engineer"
)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Button ----------
st.markdown('<div class="center">', unsafe_allow_html=True)
generate = st.button("🚀 Generate Learning Roadmap")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Roadmap Generation ----------
if generate:

    if career_goal:

        resume_file = st.session_state.resume

        with st.spinner("Extracting resume text..."):
            resume_text = extract_text_from_pdf(resume_file)

        prompt = f"""
Analyze this resume and generate a learning roadmap to become a {career_goal}.

Resume:
{resume_text}

Provide:
1. Missing Skills
2. Step-by-step learning roadmap
3. Recommended tools or technologies to learn
"""

        with st.spinner("Generating AI learning roadmap..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}]
            )

            roadmap = response.choices[0].message.content

        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📚 Your Learning Roadmap")

        st.write(roadmap)

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("Please enter your target job role.")

