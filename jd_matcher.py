from groq import Groq

# Hardcoded API key (for testing)
import os


api_key = os.getenv("GROQ_API_KEY")   # get key from environment
client = Groq(api_key=api_key)

def analyze_resume_with_jd(resume_text, job_description):
    prompt = f"""
You are an expert HR recruiter and ATS engine.

Compare the RESUME with the JOB DESCRIPTION.

Provide output in this format:

1. ATS Match Score (0-100%)
2. Hiring Chance (Low / Medium / High) with percentage
3. Matching Skills
4. Missing Skills
5. Resume Weak Points
6. Resume Improvements Needed
7. Suggested Enhancements (projects, keywords, formatting)
8. Final HR Verdict

JOB DESCRIPTION:
{job_description}

RESUME:
{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a professional recruiter and ATS expert."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=800
    )

    return response.choices[0].message.content
