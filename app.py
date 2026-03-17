import streamlit as st

st.set_page_config(page_title="TalentMatch AI", page_icon="🚀", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

/* Hide Streamlit UI */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
[data-testid="stSidebar"] {display:none;}
[data-testid="collapsedControl"] {display:none;}

/* Background Gradient */
.stApp{
background: linear-gradient(135deg,#eef2ff,#f8fafc);
}

/* Hero Section */
.hero{
font-size:70px;
font-weight:800;
background: linear-gradient(90deg,#4f46e5,#06b6d4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.sub{
font-size:20px;
color:#555;
margin-bottom:30px;
}

/* Buttons */
.stButton>button{
border-radius:12px;
width:190px;
height:48px;
font-size:17px;
font-weight:600;
border:none;
background:linear-gradient(90deg,#4f46e5,#06b6d4);
color:white;
transition:0.3s;
}

.stButton>button:hover{
transform:scale(1.05);
box-shadow:0 8px 20px rgba(0,0,0,0.2);
}

/* Feature Cards */
.card{
padding:25px;
border-radius:18px;
background:rgba(255,255,255,0.8);
backdrop-filter:blur(10px);
box-shadow:0 10px 25px rgba(0,0,0,0.08);
text-align:center;
height:210px;
display:flex;
flex-direction:column;
justify-content:center;
transition:0.3s;
}

.card:hover{
transform:translateY(-8px);
box-shadow:0 20px 35px rgba(0,0,0,0.15);
}

.card h3{
margin-bottom:10px;
}

.card p{
color:#555;
}

/* Metrics Style */
[data-testid="stMetricValue"]{
font-size:28px;
font-weight:700;
}

[data-testid="stMetricLabel"]{
font-size:16px;
}

.footer{
text-align:center;
color:#666;
padding-top:20px;
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

    with c1:
        if st.button("📝 Sign Up"):
            st.switch_page("pages/1_signup_page.py")

    with c2:
        if st.button("🔑 Login"):
            st.switch_page("pages/login_page.py")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=380)

st.write("")
st.write("")


# ---------- FEATURES ----------
st.subheader("✨ Powerful Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <h3>📄 Resume Analyzer</h3>
    <p>Upload your resume and get instant AI feedback with skill detection.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h3>🎯 Job Matching</h3>
    <p>Compare your resume with job descriptions and calculate match score.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h3>📊 Skill Gap Analysis</h3>
    <p>Identify missing skills and get recommendations to improve.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")


# ---------- METRICS ----------
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
    "The skill gap analysis showed me exactly what I needed to learn."
    <br><br>
    <b>- Data Analyst</b>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("")


# ---------- FOOTER ----------
st.markdown(
"""
<div class="footer">
Made with ❤️ using AI Career Assistant
</div>
""",
unsafe_allow_html=True
)