import streamlit as st
from db import login   # 👈 import database function

st.set_page_config(page_title="Login", page_icon="🔑", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#eef2ff,#f8fafc);
}

.title{
text-align:center;
font-size:36px;
font-weight:700;
margin-bottom:25px;
background: linear-gradient(90deg,#6366f1,#06b6d4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.stTextInput>div>div>input{
border-radius:10px;
height:40px;
}

.stButton>button{
width:100%;
height:42px;
border-radius:10px;
font-weight:600;
background: linear-gradient(90deg,#6366f1,#06b6d4);
color:white;
border:none;
}

.stButton>button:hover{
opacity:0.9;
}

</style>
""", unsafe_allow_html=True)

# ---------- Layout ----------
left, center, right = st.columns([1,2,1])

with center:

    st.markdown('<div class="title">🔑 Login</div>', unsafe_allow_html=True)

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if email and password:

            user = login(email, password)   # 👈 check from database

            if user:
                # ✅ store session
                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.user_name = user["name"]

                st.success("Login Successful!")
                st.switch_page("pages/dashboard_page.py")

            else:
                st.error("Invalid email or password")

        else:
            st.warning("Enter email and password")

    st.write("")

    if st.button("⬅ Back"):
        st.switch_page("app.py")