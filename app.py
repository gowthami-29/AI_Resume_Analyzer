import streamlit as st

st.set_page_config(page_title="AI Career Assistant", page_icon="🚀", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

/* Hide Streamlit UI */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
[data-testid="stSidebar"] {display:none;}
[data-testid="collapsedControl"] {display:none;}

/* Background */
.stApp {
    background: linear-gradient(135deg,#eef2ff,#f8fafc);
}

/* Hero title */
.hero{
    font-size:60px;
    font-weight:700;
}

/* Subtitle */
.sub{
    font-size:20px;
    color:#555;
}

/* Card */
.card{
    padding:25px;
    border-radius:15px;
    background:white;
    box-shadow:0 4px 15px rgba(0,0,0,0.08);
    text-align:center;

    height:200px;
    display:flex;
    flex-direction:column;
    justify-content:center;
}

.card h3{
    margin-bottom:10px;
}

.card p{
    margin:0;
}

/* Button */
.stButton>button{
    border-radius:10px;
    width:180px;
    height:45px;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
col1, col2 = st.columns([3,2])

with col1:

    st.markdown('<div class="hero">🚀 AI Career Assistant</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="sub">AI-powered Resume Analysis and Job Matching Platform</div>',
        unsafe_allow_html=True
    )

    c1, c2 = st.columns(2)

    with c2:
        if st.button("🔑 Login"):
            st.switch_page("pages/login_page.py")

    with c1:
        if st.button("📝 Sign Up"):
            st.switch_page("pages/1_signup_page.py")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=350)

st.write("")
st.write("")


# ---------- FEATURES ----------
st.subheader("✨ Powerful Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📄 Resume Analyzer</h3>
    <p>Upload your resume and get instant AI feedback.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🎯 Job Matching</h3>
    <p>Find jobs that match your skills and experience.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>📊 Skill Gap Analysis</h3>
    <p>Identify missing skills and improve your profile.</p>
    </div>
    """, unsafe_allow_html=True)


st.write("")
st.write("")

# ---------- TRUST SECTION ----------
st.subheader("🌍 Trusted by Career Seekers")

col1, col2, col3, col4 = st.columns(4)

col1.metric("👥 Users", "5,000+")
col2.metric("📄 Resumes Analyzed", "12,000+")
col3.metric("🎯 Job Matches", "3,500+")
col4.metric("⭐ Satisfaction", "96%")

st.write("")
st.write("")



# ---------- TESTIMONIALS ----------
st.subheader("💬 What Users Say")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
    ⭐⭐⭐⭐⭐  
    "This platform helped me improve my resume and land interviews."
    <br><br>
    <b>- Software Engineer</b>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    ⭐⭐⭐⭐⭐  
    "The skill gap analysis helped me know what to learn next."
    <br><br>
    <b>- Data Analyst</b>
    </div>
    """, unsafe_allow_html=True)


st.write("")
st.write("")


# ---------- FOOTER ----------
st.markdown(
"""
<center>
Made with ❤️ using AI Career Assistant
</center>
""",
unsafe_allow_html=True
)