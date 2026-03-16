
import streamlit as st
import os
import tempfile
from dotenv import load_dotenv
from groq import Groq
from gtts import gTTS
from streamlit_mic_recorder import mic_recorder
from resume_parser import extract_text_from_pdf

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="AI Voice Mock Interview", page_icon="🎤")

st.title("🎤 AI Resume-Based Mock Interview")

st.write("AI will ask interview questions based on your resume. Answer using your voice.")

# check resume uploaded from dashboard
if "resume" not in st.session_state:
    st.warning("Please upload your resume from the dashboard first.")
    st.stop()

resume_file = st.session_state.resume
resume_text = extract_text_from_pdf(resume_file)

# generate interview question
if st.button("Start Interview"):

    prompt = f"""
    You are an AI interviewer.

    Based on the following resume, ask ONE technical interview question.

    Resume:
    {resume_text}

    Only return the question.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    question = response.choices[0].message.content

    st.session_state.question = question

# show question
if "question" in st.session_state:

    question = st.session_state.question

    st.subheader("Interview Question")
    st.write(question)

    # AI speaks question
    tts = gTTS(question)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_file = fp.name

    st.audio(audio_file)

    st.write("🎤 Record your answer:")

    audio = mic_recorder(
        start_prompt="Start Recording",
        stop_prompt="Stop Recording",
        just_once=True
    )

    if audio:

        # save recorded voice
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio["bytes"])
            audio_path = f.name

        st.success("Voice recorded!")

        # speech-to-text using Whisper
        with open(audio_path, "rb") as file:
            transcript = client.audio.transcriptions.create(
                file=file,
                model="whisper-large-v3"
            )

        user_answer = transcript.text

        st.subheader("Your Answer")
        st.write(user_answer)

        # AI evaluates answer
        prompt = f"""
        Evaluate this interview answer.

        Question:
        {question}

        Answer:
        {user_answer}

        Provide:
        1. Score out of 10
        2. Feedback to improve
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        feedback = response.choices[0].message.content

        st.subheader("AI Feedback")
        st.write(feedback)

