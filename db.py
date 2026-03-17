import os
from dotenv import load_dotenv
from supabase import create_client
import bcrypt

load_dotenv()

# ✅ Load from .env
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

# ---------------- SIGNUP ----------------
def signup(name, email, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    return supabase.table("userssss").insert({
        "name": name,
        "email": email,
        "password": hashed
    }).execute()


# ---------------- LOGIN ----------------
def login(email, password):
    res = supabase.table("userssss").select("*").eq("email", email).execute()

    if res.data:
        user = res.data[0]
        if bcrypt.checkpw(password.encode(), user["password"].encode()):
            return user
    return None


# ---------------- SAVE RESUME ----------------
def save_resume(user_id, text, score):
    supabase.table("resumes").insert({
        "user_id": user_id,
        "resume_text": text,
        "score": score
    }).execute()