
import streamlit as st
import json
import os

st.set_page_config(page_title="Create Account", page_icon="📝", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.stApp {
background: linear-gradient(135deg,#eef2ff,#f8fafc);
}

.form-card {
background: white;
padding: 40px;
border-radius: 16px;
box-shadow: 0 12px 35px rgba(0,0,0,0.12);
}

.title {
text-align: center;
font-size: 34px;
font-weight: 700;
margin-bottom: 25px;
background: linear-gradient(90deg,#6366f1,#06b6d4);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
}

.stTextInput>div>div>input {
border-radius: 10px;
height: 40px;
}

.stButton>button {
width: 100%;
height: 42px;
border-radius: 10px;
font-weight: 600;
background: linear-gradient(90deg,#6366f1,#06b6d4);
color: white;
border: none;
}

.stButton>button:hover {
opacity: 0.9;
}

</style>
""", unsafe_allow_html=True)

# ---------- Users File ----------
if not os.path.exists("users.json"):
    with open("users.json", "w") as f:
        json.dump({"users": []}, f)

# ---------- Layout ----------
col1, col2, col3 = st.columns([1,2,1])

with col2:

    st.markdown('<div class="title">📝 Create Account</div>', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):

        if name and email and password:

            with open("users.json") as f:
                data = json.load(f)

            # check if user already exists
            for user in data["users"]:
                if user["email"] == email:
                    st.error("User already exists. Please login.")
                    st.stop()

            # add new user
            data["users"].append({
                "name": name,
                "email": email,
                "password": password
            })

            with open("users.json", "w") as f:
                json.dump(data, f, indent=4)

            st.success("Account created successfully!")
            st.switch_page("pages/login_page.py")

        else:
            st.warning("Fill all fields")

    st.write("")

    if st.button("⬅ Back"):
        st.switch_page("app.py")

