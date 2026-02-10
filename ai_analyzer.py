import os
from groq import Groq




api_key = os.getenv("GROQ_API_KEY")   # get key from environment
client = Groq(api_key=api_key)

def analyze_resume(resume_text):
    prompt = f"""
    Analyze resume and give:
    Skills, Experience Level, Best Job Role, Resume Score, Suggestions.
    Resume: {resume_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}],
        max_tokens=400
    )
    return response.choices[0].message.content
