
import streamlit as st
if "logged_in" not in st.session_state:
    st.warning("please login first")
    st.switch_page("pages/login_page.py")
st.set_page_config(page_title="AI Career Assistant", page_icon="🚀", layout="wide")

st.markdown("""
<style>

/* Header */

.header{
text-align:center;
font-size:48px;
font-weight:800;
margin-bottom:30px;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

/* Resume Upload Card */

.resume-card{
padding:20px;
border-radius:15px;
background:#ffffff;
box-shadow:0 5px 20px rgba(0,0,0,0.1);
margin-bottom:40px;
}

/* Tool Card */

.tool-box{
height:170px;
padding:20px;
border-radius:18px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
font-size:22px;
font-weight:600;
color:white;
margin-bottom:10px;
transition:0.3s;
}

.tool-box:hover{
transform:translateY(-6px);
box-shadow:0px 10px 25px rgba(0,0,0,0.2);
}

/* gradients */

.resume{background:linear-gradient(135deg,#667eea,#764ba2);}
.jd{background:linear-gradient(135deg,#f093fb,#f5576c);}
.skill{background:linear-gradient(135deg,#4facfe,#00f2fe);}
.interview{background:linear-gradient(135deg,#43e97b,#38f9d7);}
.score{background:linear-gradient(135deg,#fa709a,#fee140);}
.ats{background:linear-gradient(135deg,#30cfd0,#330867);}
.cover{background:linear-gradient(135deg,#ff9a9e,#fad0c4);}
.chatbot{background:linear-gradient(135deg,#5ee7df,#b490ca);}
.roadmap{background:linear-gradient(135deg,#f6d365,#fda085);}

/* Center Button */

.button-center{
display:flex;
justify-content:center;
margin-bottom:30px;
}

.stButton button{
width:150px;
border-radius:10px;
height:40px;
font-weight:600;
background:#111;
color:white;
}

.stButton button:hover{
background:#0072ff;
color:white;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="header">🚀 AI Career Assistant</div>', unsafe_allow_html=True)

# ---------- Resume Upload Section ----------

st.markdown('<div class="resume-card">', unsafe_allow_html=True)

st.write("### 📄 Upload Resume (Upload once and all tools will use it)")

col1, col2 = st.columns([3,1])

with col1:
    file = st.file_uploader("Upload Resume PDF", type=["pdf"])

    if file:
        st.session_state.resume = file
        st.success("✅ Resume uploaded successfully!")

with col2:
    if "resume" in st.session_state:
        st.success("Resume Stored")
    else:
        st.warning("No Resume")

st.markdown('</div>', unsafe_allow_html=True)

st.subheader("🎯 Choose a Tool")

# -------- Row 1 --------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="tool-box resume">📄 Resume Analyzer</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="resume_tool"):
        st.switch_page("pages/resume_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

with col2:
    st.markdown('<div class="tool-box jd">📊 Resume vs Job Description</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="jd"):
        st.switch_page("pages/jd_matcher_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

with col3:
    st.markdown('<div class="tool-box skill">🧠 Skill Gap Analyzer</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="skill"):
        st.switch_page("pages/skill_gap_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

# -------- Row 2 --------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="tool-box interview">💬 Interview Questions</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="interview"):
        st.switch_page("pages/interview_questions_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

with col2:
    st.markdown('<div class="tool-box score">⭐ Resume Score</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="score"):
        st.switch_page("pages/resume_score_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

with col3:
    st.markdown('<div class="tool-box ats">🤖 ATS Checker</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="ats"):
        st.switch_page("pages/ats_checker_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

# -------- Row 3 --------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="tool-box chatbot">🤖 Career Chatbot</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="chatbot"):
        st.switch_page("pages/carreer_chatbot_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

with col2:
    st.markdown('<div class="tool-box cover">✉️ Cover Letter Generator</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="cover"):
        st.switch_page("pages/cover_letter_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

with col3:
    st.markdown('<div class="tool-box roadmap">📈 Job Recommendation</div>',unsafe_allow_html=True)
    st.markdown('<div class="button-center">',unsafe_allow_html=True)
    if st.button("Open",key="job"):
        st.switch_page("pages/job_recommendation_page.py")
    st.markdown('</div>',unsafe_allow_html=True)

st.write("---")

# ---------- Logout ----------
if st.button("🔓 Logout"):
    st.session_state.clear()
    st.switch_page("app.py")

