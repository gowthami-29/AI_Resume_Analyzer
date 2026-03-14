import streamlit as st

st.title("📝 Create Account")

name = st.text_input("Full Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Create Account"):

    if name and email and password:
        st.success("Account created successfully!")
        st.switch_page("pages/login_page.py")

    else:
        st.warning("Fill all fields")

if st.button("⬅ Back"):
    st.switch_page("app.py")