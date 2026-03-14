import streamlit as st
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Learning Roadmap", page_icon="📚")

st.title("📚 AI Learning Roadmap Generator")

st.write("Get a learning roadmap based on your resume and career goals.")

resume_text = st.text_area("Paste Resume Content")

career_goal = st.text_input("Target Job Role (Example: Data Scientist)")

if st.button("Generate Roadmap"):

    if resume_text and career_goal:

        prompt = f"""
        Analyze this resume and generate a learning roadmap
        to become a {career_goal}.

        Resume:
        {resume_text}

        Provide:
        1. Missing Skills
        2. Step-by-step learning roadmap
        """

        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {"role": "user", "content": prompt}
            ]

        )

        roadmap = response.choices[0].message.content

        st.subheader("Learning Roadmap")

        st.write(roadmap)

    else:
        st.warning("Please fill all fields")