import streamlit as st
import base64

st.set_page_config(page_title="AI Career Assistant", layout="centered")

# Convert video to base64
def video_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

video_base64 = video_to_base64("vi.mp4")

# ================= CSS + VIDEO =================
st.markdown(f"""
<style>

/* Background Video */
#bg-video {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    z-index: -3;
    pointer-events: none;
}}

/* Dark overlay */
.overlay {{
    position: fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    background: rgba(0,0,0,0.65);
    z-index:-2;
}}

/* Transparent Streamlit app */
.stApp {{
    background: transparent;
}}

/* Decorative Title Box */
.title-box {{
    background: linear-gradient(135deg, rgba(255,255,255,0.15), rgba(255,255,255,0.05));
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 25px;
    border: 2px solid rgba(255,255,255,0.25);
    box-shadow: 0 0 25px rgba(255, 0, 128, 0.5);
    backdrop-filter: blur(12px);
    text-align: center;
}}

/* Main Title */
.title-box h1 {{
    color: white;
    font-size: 40px;
    font-weight: 900;
}}

/* Subtitle */
.title-box h3 {{
    color: #ffccff;
    font-size: 20px;
}}

/* Center buttons styling */
.stButton button {{
    background: linear-gradient(135deg, #ff512f, #dd2476);
    color: white;
    border-radius: 14px;
    padding: 14px;
    font-size: 18px;
    font-weight: bold;
    width: 100%;
    border: none;
    box-shadow: 0px 10px 20px rgba(0,0,0,0.4);
    transition: 0.3s;
}}

.stButton button:hover {{
    transform: scale(1.05);
    background: linear-gradient(135deg, #ffb347, #ffcc33);
    color: black;
}}

</style>

<video id="bg-video" autoplay muted loop>
<source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
</video>

<div class="overlay"></div>
""", unsafe_allow_html=True)

# ================= TITLE BOX =================
st.markdown("""
<div class="title-box">
    <h1>🚀 AI Career Assistant System</h1>
    <h3>Smart Resume Analyzer & Job Matching Platform</h3>
</div>
""", unsafe_allow_html=True)

# ================= CENTER BUTTONS =================
# Create 3 columns (left space, center buttons, right space)
left, center, right = st.columns([4,4,4])

with center:
    if st.button("\u00A0\u00A0\u00A0\u00A0\u00A0📄 \u00A0\u00A0Resume     \u00A0\u00A0     Analyzer\u00A0\u00A0\u00A0"):
        st.switch_page("pages/resume_page.py")

    if st.button("💼 Job Description Matcher"):
        st.switch_page("pages/jd_matcher_page.py")
