import streamlit as st
import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="Canva Resume Builder", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.main-title{
text-align:center;
font-size:45px;
font-weight:800;
background: linear-gradient(90deg,#4f46e5,#06b6d4);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.preview-box{
padding:20px;
border-radius:15px;
background:white;
box-shadow:0 10px 25px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<div class="main-title">🎨 Canva Resume Builder</div>', unsafe_allow_html=True)

# ---------- TEMPLATE ----------
template = st.radio(
    "Choose Template",
    ["Modern", "Professional", "Minimal"],
    horizontal=True
)

# ---------- LAYOUT ----------
col1, col2 = st.columns([1,1])

# ---------- INPUT ----------
with col1:
    st.subheader("✏️ Edit Your Resume")

    name = st.text_input("Full Name", "Your Name")
    email = st.text_input("Email", "your@email.com")
    phone = st.text_input("Phone", "1234567890")

    skills = st.text_area("Skills", "Python, SQL, Machine Learning")
    education = st.text_area("Education", "B.Tech in Computer Science")
    experience = st.text_area("Experience", "Fresher / Internship details")
    projects = st.text_area("Projects", "AI Resume Analyzer Project")

# ---------- PREVIEW ----------
with col2:
    st.subheader("📄 Live Preview")

    if template == "Modern":
        st.markdown(f"""
        <div class="preview-box">
        <h2 style="color:#4f46e5;">{name}</h2>
        <p>{email} | {phone}</p>
        <hr>

        <h4>Skills</h4>
        <p>{skills}</p>

        <h4>Education</h4>
        <p>{education}</p>

        <h4>Experience</h4>
        <p>{experience}</p>

        <h4>Projects</h4>
        <p>{projects}</p>
        </div>
        """, unsafe_allow_html=True)

    elif template == "Professional":
        st.markdown(f"""
        <div class="preview-box">
        <h2>{name}</h2>
        <p><b>Email:</b> {email} | <b>Phone:</b> {phone}</p>
        <hr>

        <h4>Skills</h4>
        <p>{skills}</p>

        <h4>Education</h4>
        <p>{education}</p>

        <h4>Experience</h4>
        <p>{experience}</p>

        <h4>Projects</h4>
        <p>{projects}</p>
        </div>
        """, unsafe_allow_html=True)

    elif template == "Minimal":
        st.markdown(f"""
        <div class="preview-box">
        <h3>{name}</h3>
        <p>{email} | {phone}</p>

        <p><b>Skills:</b> {skills}</p>
        <p><b>Education:</b> {education}</p>
        <p><b>Experience:</b> {experience}</p>
        <p><b>Projects:</b> {projects}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------- PDF FUNCTION ----------
def create_pdf(data):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph(f"<b>{data['name']}</b>", styles["Title"]))
    content.append(Spacer(1, 10))
    content.append(Paragraph(f"{data['email']} | {data['phone']}", styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Skills</b>", styles["Heading2"]))
    content.append(Paragraph(data["skills"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Education</b>", styles["Heading2"]))
    content.append(Paragraph(data["education"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Experience</b>", styles["Heading2"]))
    content.append(Paragraph(data["experience"], styles["Normal"]))
    content.append(Spacer(1, 10))

    content.append(Paragraph("<b>Projects</b>", styles["Heading2"]))
    content.append(Paragraph(data["projects"], styles["Normal"]))

    doc.build(content)
    buffer.seek(0)
    return buffer

# ---------- DOWNLOAD ----------
st.write("---")

data = {
    "name": name,
    "email": email,
    "phone": phone,
    "skills": skills,
    "education": education,
    "experience": experience,
    "projects": projects
}

pdf_file = create_pdf(data)

st.download_button(
    "📥 Download Resume (PDF)",
    data=pdf_file,
    file_name="resume.pdf",
    mime="application/pdf"
)