# app.py
# Personal portfolio built with Streamlit.
# Edit the CONFIG section below with your own information, then deploy to
# Streamlit Community Cloud by pushing this file (and requirements.txt) to GitHub.

import streamlit as st

# ---------------------------------------------------------------------------
# CONFIG — edit everything in this section with your own information
# ---------------------------------------------------------------------------
NAME = "백준서"
TITLE = "Data Scientist / ML Engineer"
BIO = (
    "데이터로 문제를 해결하는 것을 좋아하는 개발자입니다. "
    "머신러닝, 데이터 시각화, 웹 애플리케이션 개발에 관심이 많습니다."
)
EMAIL = "youg74@naver.com"
GITHUB_URL = "https://github.com/your-username"
LINKEDIN_URL = "https://linkedin.com/in/your-profile"
RESUME_URL = ""  # Optional: link to a PDF resume hosted somewhere (e.g. GitHub raw link)

SKILLS = [
    "Python", "SQL", "Pandas / NumPy", "Scikit-learn",
    "PyTorch / TensorFlow", "Streamlit", "Git / GitHub", "Docker",
]
CERTIFICATIONS = [
    {
        "name": "Microsoft Azure Fundamentals (AZ-900)",
        "issuer": "Microsoft",
        "date": "",  # 취득일 입력
    },
    {
        "name": "빅데이터분석실무 2급",
        "issuer": "한국데이터산업진흥원",
        "date": "",  # 취득일 입력
    },
    {
        "name": "DSAC-M1",
        "issuer": "",  # 발급기관 입력
        "date": "",  # 취득일 입력
    },
]

PROJECTS = [
    {
        "title": "초미세먼지 예측 및 위험도 안내 시스템",
        "description": (
            "에어코리아·기상청 공공데이터(전국 17개 시도, 3년치)를 수집·전처리하여 "
            "XGBoost 머신러닝 모델로 내일 PM2.5 농도를 예측하는 AI 시스템입니다. "
            "위험 등급 자동 분류, 행동 가이드, "
            "Streamlit Cloud를 통해 모바일 웹으로 배포하였습니다."
        ),
        "tags": ["Python", "XGBoost", "Streamlit", "Pandas", "공공데이터"],
        "link": "",
        "github": "",
    },
    {
        "title": "프로젝트 이름을 입력하세요",
        "description": "프로젝트에 대한 간단한 설명을 2~3문장으로 작성하세요.",
        "tags": ["태그1", "태그2"],
        "link": "",
        "github": "",
    },
]
# ---------------------------------------------------------------------------
# PAGE SETUP
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="👋",
    layout="wide",
)

# Minimal custom styling
st.markdown(
    """
    <style>
        .main > div { padding-top: 2rem; }
        .project-card {
            border: 1px solid #333;
            border-radius: 10px;
            padding: 1.2rem 1.4rem;
            margin-bottom: 1rem;
        }
        .project-tag {
            display: inline-block;
            background-color: #2a2e33;
            color: #f5f1e8;
            border-radius: 4px;
            padding: 0.15rem 0.6rem;
            font-size: 0.78rem;
            margin-right: 0.4rem;
        }
        .section-title {
            margin-top: 2.2rem;
            margin-bottom: 0.8rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"## {NAME}")
    st.caption(TITLE)
    st.write(BIO)

    st.markdown("---")
    st.markdown(f"[GitHub]({GITHUB_URL})")
    st.markdown(f"[LinkedIn]({LINKEDIN_URL})")
    st.markdown(f"[Email](mailto:{EMAIL})")
    if RESUME_URL:
        st.markdown(f"[이력서 (PDF)]({RESUME_URL})")

    st.markdown("---")
    page = st.radio("메뉴", ["소개", "프로젝트", "연락처"], label_visibility="collapsed")

# ---------------------------------------------------------------------------
# PAGE: 소개 (About)
# ---------------------------------------------------------------------------
if page == "소개":
    st.title(f"안녕하세요, {NAME}입니다 👋")
    st.subheader(TITLE)
    st.write(BIO)

    st.markdown("<div class='section-title'></div>", unsafe_allow_html=True)
    st.markdown("### Skills")
    cols = st.columns(4)
    for i, skill in enumerate(SKILLS):
        with cols[i % 4]:
            st.markdown(f"- {skill}")

# ---------------------------------------------------------------------------
# PAGE: 프로젝트 (Projects)
# ---------------------------------------------------------------------------
elif page == "프로젝트":
    st.title("프로젝트")
    st.write("진행했던 프로젝트들을 소개합니다.")

    for project in PROJECTS:
        with st.container():
            st.markdown("<div class='project-card'>", unsafe_allow_html=True)
            st.markdown(f"#### {project['title']}")
            st.write(project["description"])

            tags_html = "".join(
                f"<span class='project-tag'>{tag}</span>" for tag in project["tags"]
            )
            st.markdown(tags_html, unsafe_allow_html=True)

            link_cols = st.columns(2)
            with link_cols[0]:
                if project.get("link"):
                    st.markdown(f"[🔗 데모 보기]({project['link']})")
            with link_cols[1]:
                if project.get("github"):
                    st.markdown(f"[💻 코드 보기]({project['github']})")

            st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# PAGE: 연락처 (Contact)
# ---------------------------------------------------------------------------
elif page == "연락처":
    st.title("연락처")
    st.write("편하게 연락 주세요!")

    st.markdown(f"📧 **Email:** [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"💻 **GitHub:** [{GITHUB_URL}]({GITHUB_URL})")
    st.markdown(f"🔗 **LinkedIn:** [{LINKEDIN_URL}]({LINKEDIN_URL})")

    st.markdown("---")
    st.markdown("#### 메시지 남기기")
    with st.form("contact_form"):
        sender_name = st.text_input("이름")
        sender_email = st.text_input("이메일")
        message = st.text_area("메시지")
        submitted = st.form_submit_button("보내기")
        if submitted:
            # NOTE: This form does not actually send an email by itself.
            # To make it functional, connect it to a service such as
            # Formspree, EmailJS, or a simple backend endpoint.
            st.success("메시지가 기록되었습니다. (실제 전송을 위해서는 외부 서비스 연동이 필요합니다)")
