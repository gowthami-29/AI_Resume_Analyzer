import os
from groq import Groq
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)

def analyze_resume(resume_text):
    prompt = f"""
    Analyze resume and give:
    Skills, Experience Level, Best Job Role, Resume Score, Suggestions.
    Resume: {resume_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400
    )

    return response.choices[0].message.content
