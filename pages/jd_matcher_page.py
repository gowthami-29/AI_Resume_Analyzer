import streamlit as st
import base64
from resume_parser import extract_text_from_pdf
from jd_matcher import analyze_resume_with_jd

# Page config
st.set_page_config(page_title="Resume Matcher", layout="centered")

# Cache background to prevent reload flicker
@st.cache_data
def get_base64_bg(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64_bg("pages/r1.png")



# Display the title
st.title("💼 Resume vs JD Matcher")


uploaded_resume = st.file_uploader("📄 Upload Resume PDF", type=["pdf"])
job_description = st.text_area("📋 Paste Job Description", height=150)

if uploaded_resume and job_description:
    resume_text = extract_text_from_pdf(uploaded_resume)

    if st.button("🔍 Match Resume with JD"):
        with st.spinner("Analyzing Resume vs Job Description..."):
            result = analyze_resume_with_jd(resume_text, job_description)

        st.subheader("📊 ATS Matching Result")
        st.write(result)
