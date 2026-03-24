import streamlit as st
from db import supabase

# ---------- PROTECT ----------
if "user" not in st.session_state:
    st.warning("Please login first")
    st.switch_page("pages/login_page.py")

user = st.session_state.user

st.set_page_config(page_title="AI Resume Assistant", page_icon="🚀", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

/* HEADER */
.header{
text-align:center;
font-size:50px;
font-weight:800;
background: linear-gradient(90deg,#4f46e5,#06b6d4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.sub{
text-align:center;
color:#666;
margin-bottom:30px;
}

/* CARD CONTAINER */
.tool-container{
padding:25px;
border-radius:20px;
color:white;
text-align:center;
box-shadow:0 10px 30px rgba(0,0,0,0.15);
transition:0.3s;
margin-bottom:15px;
}

.tool-container:hover{
transform:translateY(-8px);
box-shadow:0 20px 40px rgba(0,0,0,0.25);
}

/* COLORS */
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

/* BUTTON */
.stButton button{
width:120px;
height:38px;
border-radius:10px;
background:#111;
color:white;
font-weight:600;
display:block;
margin:12px auto;
}

.stButton button:hover{
background:#0072ff;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="header">🚀 AI Resume Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Your AI Powered Career Platform</div>', unsafe_allow_html=True)

st.write(f"### Welcome 👋 {user['name']}")

# ---------- UPLOAD ----------
st.subheader("📄 Upload Resume")

col1, col2 = st.columns([3,1])

with col1:
    file = st.file_uploader("Upload Resume", type=["pdf"])
    if file:
        st.session_state.resume = file
        st.success("Resume uploaded!")

with col2:
    if "resume" in st.session_state:
        st.success("Stored")
    else:
        st.warning("No Resume")

st.write("---")

# ---------- TOOL FUNCTION ----------
def tool_card(title, css_class, page, key):
    st.markdown(f"""
    <div class="tool-container {css_class}">
        <h3>{title}</h3>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1,2,1])
    with c2:
        if st.button("Open", key=key):
            st.switch_page(page)

# ---------- TOOLS ----------
st.subheader("🧠 AI Career Tools")

col1, col2, col3 = st.columns(3)

with col1:
    tool_card("📄 Resume Analyzer", "resume", "pages/resume_page.py", "1")

with col2:
    tool_card("📊 Career Report", "jd", "pages/career_report_page.py", "2")

with col3:
    tool_card("🧠 Skill Gap", "skill", "pages/skill_gap_page.py", "3")

col1, col2, col3 = st.columns(3)

with col1:
    tool_card("🎤 Interview Questions", "interview", "pages/interview_questions_page.py", "4")

with col2:
    tool_card("📈 Resume Score", "score", "pages/resume_score_page.py", "5")

with col3:
    tool_card("📄 ATS Checker", "ats", "pages/ats_checker_page.py", "6")

col1, col2, col3 = st.columns(3)

with col1:
    tool_card("🤖 Career Chatbot", "chatbot", "pages/carreer_chatbot_page.py", "7")

with col2:
    tool_card("✉ Cover Letter", "cover", "pages/cover_letter_page.py", "8")

with col3:
    tool_card("💼 Job Recommendation", "roadmap", "pages/job_recommendation_page.py", "9")

col1, col2, col3 = st.columns(3)

with col1:
    tool_card("📚 Learning Roadmap", "roadmap", "pages/learning_roadmap_page.py", "10")

with col2:
    tool_card("🎯 AI Mock Interview", "mock", "pages/mock_interview_voice.py", "11")

with col3:
    tool_card("🧾 Resume Builder", "cover", "pages/resume_builder.py", "12")

st.write("---")

# ---------- LOGOUT ----------
if st.button("🔓 Logout"):
    st.session_state.clear()
    st.switch_page("app.py")