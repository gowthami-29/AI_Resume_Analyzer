import streamlit as st
from db import supabase
import pandas as pd

# ---------- PROTECT ----------
if "user" not in st.session_state:
    st.warning("Please login first")
    st.switch_page("pages/login_page.py")

user = st.session_state.user

st.set_page_config(page_title="Dashboard", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>

.header{
font-size:42px;
font-weight:800;
margin-bottom:5px;
background: linear-gradient(90deg,#4f46e5,#06b6d4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.sub{
color:gray;
margin-bottom:20px;
}

/* STAT CARDS */
.card{
padding:20px;
border-radius:16px;
color:white;
font-weight:600;
box-shadow:0 8px 25px rgba(0,0,0,0.1);
}

.c1{background:linear-gradient(135deg,#6366f1,#06b6d4);}
.c2{background:linear-gradient(135deg,#f59e0b,#ef4444);}
.c3{background:linear-gradient(135deg,#10b981,#3b82f6);}

/* TOOL CARDS */
.tool{
padding:30px;
border-radius:16px;
color:white;
text-align:center;
font-weight:600;
margin-bottom:10px;
transition:0.3s;
}

.tool:hover{
transform:translateY(-6px);
box-shadow:0 10px 30px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown(f'<div class="header">👋 Welcome {user["name"]}</div>', unsafe_allow_html=True)
st.markdown('<div class="sub">Your AI Career Dashboard</div>', unsafe_allow_html=True)

# ---------- FETCH DATA ----------
res = supabase.table("resumes") \
    .select("score") \
    .eq("user_id", user["id"]) \
    .execute()

scores = [r["score"] for r in res.data]

# ---------- STATS ----------
if scores:

    col1, col2, col3 = st.columns(3)

    col1.markdown(f"""
    <div class="card c1">
    📄 Total Resumes<br><br>
    <h2>{len(scores)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col2.markdown(f"""
    <div class="card c2">
    🏆 Best Score<br><br>
    <h2>{max(scores)}</h2>
    </div>
    """, unsafe_allow_html=True)

    col3.markdown(f"""
    <div class="card c3">
    📊 Average Score<br><br>
    <h2>{int(sum(scores)/len(scores))}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ---------- GRAPH ----------
    df = pd.DataFrame({
        "Attempt": range(1, len(scores)+1),
        "Score": scores
    })

    st.subheader("📈 Resume Performance")
    st.line_chart(df.set_index("Attempt"))

else:
    st.info("No resume data yet. Analyze a resume to see insights.")

st.write("---")

