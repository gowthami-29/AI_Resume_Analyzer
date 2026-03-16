
import streamlit as st

# Protect page
if "logged_in" not in st.session_state:
    st.warning("Please login first")
    st.switch_page("pages/login_page.py")

st.set_page_config(page_title="AI Career Assistant", page_icon="🚀", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.header{
text-align:center;
font-size:50px;
font-weight:800;
margin-bottom:10px;
background: linear-gradient(90deg,#00c6ff,#0072ff);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.sub{
text-align:center;
color:gray;
margin-bottom:40px;
}



.tool-box{
height:150px;
border-radius:18px;
display:flex;
flex-direction:column;
justify-content:center;
align-items:center;
text-align:center;
font-size:20px;
font-weight:600;
color:white;
margin-bottom:10px;
transition:0.3s;
}

.tool-box:hover{
transform:translateY(-5px);
box-shadow:0px 10px 20px rgba(0,0,0,0.2);
}

.resume{background:linear-gradient(135deg,#667eea,#764ba2);}
.jd{background:linear-gradient(135deg,#f093fb,#f5576c);}
.skill{background:linear-gradient(135deg,#4facfe,#00f2fe);}
.interview{background:linear-gradient(135deg,#43e97b,#38f9d7);}
.score{background:linear-gradient(135deg,#fa709a,#fee140);}
.ats{background:linear-gradient(135deg,#30cfd0,#330867);}
.chatbot{background:linear-gradient(135deg,#5ee7df,#b490ca);}
.cover{background:linear-gradient(135deg,#ff9a9e,#fad0c4);}
.roadmap{background:linear-gradient(135deg,#f6d365,#fda085);}
.mock{background:linear-gradient(135deg,#ff7eb3,#ff758c);}

.button-center{
display:flex;
justify-content:center;
margin-bottom:30px;
}

.stButton button{
width:140px;
height:38px;
border-radius:10px;
background:#111;
color:white;
font-weight:600;
}

.stButton button:hover{
background:#0072ff;
}

</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="header">🚀 AI Career Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Your AI Powered Career Platform</div>', unsafe_allow_html=True)

# Welcome
st.write(f"### Welcome 👋 {st.session_state.user_email}")

# ---------- Resume Upload ----------
st.markdown('<div class="resume-card">', unsafe_allow_html=True)

st.write("### 📄 Upload Resume (One time upload for all tools)")

col1, col2 = st.columns([3,1])

with col1:
    file = st.file_uploader("Upload Resume", type=["pdf"])

    if file:
        st.session_state.resume = file
        st.success("Resume uploaded successfully!")

with col2:
    if "resume" in st.session_state:
        st.success("Resume Stored")
    else:
        st.warning("No Resume")

st.markdown('</div>', unsafe_allow_html=True)

st.subheader("🧠 AI Career Tools")

# ---------- Row 1 ----------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="tool-box resume">Resume Analyzer</div>',unsafe_allow_html=True)
    if st.button("Open",key="1"):
        st.switch_page("pages/resume_page.py")

with col2:
    st.markdown('<div class="tool-box jd">Resume vs JD</div>',unsafe_allow_html=True)
    if st.button("Open",key="2"):
        st.switch_page("pages/jd_matcher_page.py")

with col3:
    st.markdown('<div class="tool-box skill">Skill Gap</div>',unsafe_allow_html=True)
    if st.button("Open",key="3"):
        st.switch_page("pages/skill_gap_page.py")

# ---------- Row 2 ----------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="tool-box interview">Interview Questions</div>',unsafe_allow_html=True)
    if st.button("Open",key="4"):
        st.switch_page("pages/interview_questions_page.py")

with col2:
    st.markdown('<div class="tool-box score">Resume Score</div>',unsafe_allow_html=True)
    if st.button("Open",key="5"):
        st.switch_page("pages/resume_score_page.py")

with col3:
    st.markdown('<div class="tool-box ats">ATS Checker</div>',unsafe_allow_html=True)
    if st.button("Open",key="6"):
        st.switch_page("pages/ats_checker_page.py")

# ---------- Row 3 ----------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="tool-box chatbot">Career Chatbot</div>',unsafe_allow_html=True)
    if st.button("Open",key="7"):
        st.switch_page("pages/carreer_chatbot_page.py")

with col2:
    st.markdown('<div class="tool-box cover">Cover Letter</div>',unsafe_allow_html=True)
    if st.button("Open",key="8"):
        st.switch_page("pages/cover_letter_page.py")

with col3:
    st.markdown('<div class="tool-box roadmap">Job Recommendation</div>',unsafe_allow_html=True)
    if st.button("Open",key="9"):
        st.switch_page("pages/job_recommendation_page.py")

# ---------- Row 4 ----------
col1,col2,col3 = st.columns(3)

with col1:
    st.markdown('<div class="tool-box roadmap">Learning Roadmap</div>',unsafe_allow_html=True)
    if st.button("Open",key="10"):
        st.switch_page("pages/learning_roadmap_page.py")

with col2:
    st.markdown('<div class="tool-box mock">AI Mock Interview</div>',unsafe_allow_html=True)
    if st.button("Open",key="11"):
        st.switch_page("pages/mock_interview_voice.py")
with col3:
    st.markdown('<div class="tool-box jd"> Career Report</div>',unsafe_allow_html=True)
    if st.button("Open",key="report"):
        st.switch_page("pages/career_report_page.py")

# ---------- Logout ----------
st.write("---")

if st.button("🔓 Logout"):
    st.session_state.clear()
    st.switch_page("app.py")
