import streamlit as st
import re
from resume_parser import extract_text_from_pdf

st.set_page_config(page_title="Skill Gap Analyzer", page_icon="🧠", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>

.title{
text-align:center;
font-size:40px;
font-weight:800;
margin-bottom:20px;
background: linear-gradient(90deg,#4facfe,#00f2fe);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.skill{
display:inline-block;
background:#e0f2fe;
padding:6px 12px;
border-radius:20px;
margin:5px;
font-size:14px;
}

.missing{
display:inline-block;
background:#fee2e2;
padding:6px 12px;
border-radius:20px;
margin:5px;
font-size:14px;
}

.center{
display:flex;
justify-content:center;
}

.stButton button{
width:200px;
height:45px;
font-size:16px;
border-radius:10px;
font-weight:600;
background:#00a8ff;
color:white;
}

.stButton button:hover{
background:#0078d4;
}

</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">🧠 Skill Gap Analyzer</div>', unsafe_allow_html=True)

# ---------- Check Resume ----------
if "resume" not in st.session_state:
    st.warning("⚠ Please upload your resume from the Dashboard first.")
    st.stop()

st.success("✅ Resume loaded successfully")

# ---------- JD Input ----------
st.subheader("📋 Paste Job Description")

jd_text = st.text_area(
    "Job Description",
    height=200,
    placeholder="Paste the job description here..."
)

# ---------- Skill Extraction ----------
def extract_skills(text):

    skills_list = [
        "python","java","c++","sql","machine learning","deep learning",
        "data science","docker","kubernetes","react","nodejs",
        "tensorflow","pytorch","aws","html","css","javascript",
        "mongodb","flask","django","pandas","numpy","git"
    ]

    text = text.lower()
    found_skills = []

    for skill in skills_list:
        # Exact match using regex (avoids java inside javascript issue)
        if re.search(rf"\b{re.escape(skill)}\b", text):
            found_skills.append(skill)

    return list(set(found_skills))

# ---------- Analyze Button ----------
st.markdown('<div class="center">', unsafe_allow_html=True)
analyze = st.button("🔍 Analyze Skill Gap")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- Analysis ----------
if analyze:

    resume_file = st.session_state.resume

    with st.spinner("Extracting resume text..."):
        resume_text = extract_text_from_pdf(resume_file)

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    missing_skills = list(set(jd_skills) - set(resume_skills))

    # ---------- Results ----------
    st.subheader("📄 Resume Skills")
    if resume_skills:
        for s in resume_skills:
            st.markdown(f'<span class="skill">{s}</span>', unsafe_allow_html=True)
    else:
        st.info("No skills detected in resume")

    st.subheader("💼 Job Required Skills")
    if jd_skills:
        for s in jd_skills:
            st.markdown(f'<span class="skill">{s}</span>', unsafe_allow_html=True)
    else:
        st.info("No skills detected in job description")

    st.subheader("❌ Missing Skills")
    if missing_skills:
        for s in missing_skills:
            st.markdown(f'<span class="missing">{s}</span>', unsafe_allow_html=True)
    else:
        st.success("🎉 Your resume already contains all required skills!")

    # ---------- Match Score ----------
    if jd_skills:
        match_percent = int((len(set(resume_skills) & set(jd_skills)) / len(jd_skills)) * 100)
        st.progress(match_percent / 100)
        st.success(f"🎯 Match Score: {match_percent}%")