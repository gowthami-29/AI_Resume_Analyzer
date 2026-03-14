import streamlit as st
import re
import spacy

# Load NLP model
nlp = spacy.load("en_core_web_sm")

st.set_page_config(page_title="Skill Gap Analyzer", page_icon="🧠")

st.title("🧠 Skill Gap Analyzer")

st.write("Compare your resume skills with job description skills")

# Upload resume text
resume_text = st.text_area("Paste Resume Text")

# Job description
jd_text = st.text_area("Paste Job Description")

# Simple skill extraction
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
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


if st.button("Analyze Skill Gap"):

    if resume_text and jd_text:

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        missing_skills = list(set(jd_skills) - set(resume_skills))

        st.subheader("📄 Resume Skills")
        st.write(resume_skills)

        st.subheader("💼 Job Required Skills")
        st.write(jd_skills)

        st.subheader("❌ Missing Skills")
        st.write(missing_skills)

    else:
        st.warning("Please paste both resume and job description")