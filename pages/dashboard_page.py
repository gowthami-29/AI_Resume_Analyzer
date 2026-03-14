import streamlit as st

st.title("🚀 AI Career Assistant Dashboard")

st.write("Choose a tool")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Resume Analyzer"):
        st.switch_page("pages/resume_page.py")

with col2:
    if st.button("Resume vs JD"):
        st.switch_page("pages/jd_matcher_page.py")

with col3:
    if st.button("Skill Gap Analyzer"):
        st.switch_page("pages/skill_gap_page.py")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Interview Questions"):
        st.switch_page("pages/interview_questions_page.py")

with col2:
    if st.button("Resume Score"):
        st.switch_page("pages/resume_score_page.py")

with col3:
    if st.button("ATS Checker"):
        st.switch_page("pages/ats_checker_page.py")
with col1: 
    if st.button(" Cover Letter Generator"):
        st.switch_page("pages/cover_letter_page.py")
with col2:
    if st.button(" Career Role Recommendation"):
        st.switch_page("pages/job_recommendation_page.py")
with col3:
    if st.button(" Learning Roadmap"):
        st.switch_page("pages/learning_roadmap_page.py") 
with col1:
    if st.button("💬 AI Career Chatbot"):
        st.switch_page("pages/carreer_chatbot_page.py") 

if st.button("Logout"):
    st.switch_page("app.py")