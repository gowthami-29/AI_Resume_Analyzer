
import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq
from resume_parser import extract_text_from_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Career Chatbot", page_icon="💬", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:800;
margin-bottom:10px;
background: linear-gradient(90deg,#667eea,#764ba2);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle{
text-align:center;
color:#555;
margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">💬 AI Career Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask anything about careers, jobs, resumes, and interviews</div>', unsafe_allow_html=True)

# ---------- Check Resume ----------
resume_text = ""

if "resume" in st.session_state:
    resume_file = st.session_state.resume
    resume_text = extract_text_from_pdf(resume_file)

# ---------- Chat History ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------- User Input ----------
prompt = st.chat_input("Ask a career question...")

if prompt:

    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    system_prompt = f"""
You are an AI career advisor helping students with:

- Resume improvement
- Job preparation
- Skill learning
- Interview preparation
- Career roadmap

Here is the user's resume (if available):

{resume_text}
"""

    with st.spinner("Thinking..."):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )

        reply = response.choices[0].message.content

    # Save AI response
    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.markdown(reply)

