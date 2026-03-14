import streamlit as st
import base64
from resume_parser import extract_text_from_pdf
from ai_analyzer import analyze_resume

# Page config
st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# Cache background to prevent reload flicker
@st.cache_data
def get_base64_bg(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = get_base64_bg("pages/r2.png")
# Display title
st.title("📄 AI Resume Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    if st.button("Analyze Resume"):
        with st.spinner("Analyzing..."):
            # Run your AI analysis
            result = analyze_resume(resume_text)

        st.subheader("📊 Resume Analysis Result")
        # Display all output via st.write
        st.write(result)
