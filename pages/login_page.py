import streamlit as st

st.title("🔑 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if email and password:
        st.success("Login Successful!")
        st.switch_page("pages/dashboard_page.py")
    else:
        st.warning("Enter email and password")

if st.button("⬅ Back"):
    st.switch_page("app.py")