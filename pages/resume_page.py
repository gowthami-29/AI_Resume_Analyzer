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

# CSS styling
st.markdown(f"""
<style>
/* Background FIXED */
.stApp {{
    background: url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}}

/* Content panel slightly to the right */
.block-container {{
    max-width: 700px;          
    margin-left: 150px;        
    margin-top: 350px;          
    background: rgba(0, 0, 0, 0.65);
    padding: 25px;
    border-radius: 18px;
    backdrop-filter: blur(8px);
}}

/* Force all text white (except file uploader and textarea) */
*:not(.stFileUploader *):not(.stFileUploader):not(.stTextArea *):not(.stTextArea) {{
    color: white !important;
}}

/* Buttons */
div.stButton > button {{
    width: 100%;
    background-color: #00b4d8;
    color: black !important;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px;
}}
div.stButton > button:hover {{
    background-color: #0077b6;
    color: white !important;
}}

/* File uploader / drag & drop */
div.stFileUploader {{
    background-color: #f0f0f0 !important;
    border: 2px dashed #00b4d8 !important;
    border-radius: 12px !important;
    padding: 15px !important;
}}
div.stFileUploader span {{
    color: #0077b6 !important;
    font-weight: bold !important;
    font-size: 16px !important;
}}
div.stFileUploader:hover {{
    background-color: #e0f7fa !important;
    border-color: #0077b6 !important;
}}

/* Page title */
h1 {{
    text-align: center !important;
    font-weight: bold !important;
    font-size: 32px !important;
    color: #00b4d8 !important;
}}
</style>
""", unsafe_allow_html=True)

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
