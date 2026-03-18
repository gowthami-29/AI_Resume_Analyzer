import streamlit as st
from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Resume Builder", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.main-title{
text-align:center;
font-size:45px;
font-weight:800;
margin-bottom:10px;
background: linear-gradient(90deg,#4f46e5,#06b6d4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.sub{
text-align:center;
color:gray;
margin-bottom:40px;
}



.stButton>button{
width:100%;
height:45px;
border-radius:12px;
font-size:16px;
font-weight:600;
background:linear-gradient(90deg,#4f46e5,#06b6d4);
color:white;
border:none;
}

.stButton>button:hover{
transform:scale(1.03);
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="main-title">🧠 ResumeCraft AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Build professional resumes in seconds</div>', unsafe_allow_html=True)

# ---------- LAYOUT ----------
col1, col2 = st.columns([1,1])

# ---------- LEFT SIDE (INPUT) ----------
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📥 Enter Your Details")

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")

    skills = st.text_area("Skills (comma separated)")
    education = st.text_area("Education")
    experience = st.text_area("Experience")
    projects = st.text_area("Projects")

    generate = st.button("🚀 Generate Resume")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------- RIGHT SIDE (OUTPUT) ----------
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📄 Resume Preview")

    if generate and name and skills:

        with st.spinner("Generating..."):

            prompt = f"""
            Create a professional resume.

            Name: {name}
            Email: {email}
            Phone: {phone}
            Skills: {skills}
            Education: {education}
            Experience: {experience}
            Projects: {projects}

            Format with proper sections.
            """

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role":"user","content":prompt}]
            )

            resume = response.choices[0].message.content

            st.write(resume)

            st.download_button(
                "📥 Download Resume",
                resume,
                file_name="resume.txt"
            )

    else:
        st.info("Fill details and click Generate")

    st.markdown('</div>', unsafe_allow_html=True)