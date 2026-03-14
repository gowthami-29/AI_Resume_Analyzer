import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Career Recommendation", page_icon="🚀")

st.title("🚀 AI Career Role Recommendation")

st.write("Get career role suggestions based on your resume.")

resume_text = st.text_area("Paste Resume Content")

if st.button("Recommend Roles"):

    if resume_text:

        prompt = f"""
        Based on the following resume, suggest 5 suitable career roles.

        Resume:
        {resume_text}

        Also give a short reason for each role.
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        result = response.choices[0].message.content

        st.subheader("Recommended Career Roles")

        st.write(result)

    else:
        st.warning("Please paste your resume")