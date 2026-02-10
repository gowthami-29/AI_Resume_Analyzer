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

st.markdown(
    f"""
    <style>
    /* Background FIXED */
    .stApp {{
        background: url("data:image/png;base64,{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        background-repeat: no-repeat;
    }}
    

    /* Center content panel */
    .block-container {{
        max-width: 600px;
        margin: auto;
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

    /* Job Description textarea */
    textarea, .stTextArea > div > div > div > textarea {{
        color: black !important;
        background-color: white !important;
        font-weight: normal !important;
    }}
    .stTextArea > div > div > div {{
        background-color: white !important;
        border-radius: 8px !important;
        padding: 5px !important;
    }}

    /* Job Description label */
    .stTextArea label {{
        color: #00b4d8 !important;   /* bright blue label text */
        font-weight: bold !important;
        font-size: 18px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Center and style the page title */
    h1 {
        text-align: center !important;   /* center horizontally */
        font-weight: bold !important;    /* make bold */
        font-size: 32px !important;      /* larger font */
        color: #00b4d8 !important;       /* blue color to stand out */
    }
    </style>
    """,
    unsafe_allow_html=True
)

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
