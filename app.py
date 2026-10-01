import streamlit as st

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
NAME = "백준서"
TITLE = "Data Scientist / ML Engineer"
BIO = (
    "데이터로 문제를 해결하는 것을 좋아하는 개발자입니다. "
    "머신러닝, 데이터 시각화, 웹 애플리케이션 개발에 관심이 많습니다."
)
GITHUB_URL = "https://github.com/your-username"
LINKEDIN_URL = "https://linkedin.com/in/your-profile"
RESUME_URL = ""

SKILLS = [
    "Python", "SQL", "Pandas / NumPy", "Scikit-learn",
    "PyTorch / TensorFlow", "Streamlit", "Git / GitHub", "Docker",
]

CERTIFICATIONS = [
    {
        "name": "Microsoft Azure Fundamentals (AZ-900)",
        "issuer": "Microsoft",
        "date": "",
    },
    {
        "name": "빅데이터분석실무 2급",
        "issuer": "한국데이터산업진흥원",
        "date": "",
    },
    {
        "name": "DSAC-M1",
        "issuer": "",
        "date": "",
    },
]

PROJECTS = [
    {
        "title": "초미세먼지 예측 및 위험도 안내 시스템",
        "description": (
            "에어코리아·기상청 공공데이터(전국 17개 시도, 3년치)를 수집·전처리하여 "
            "XGBoost 머신러닝 모델로 내일 PM2.5 농도를 예측하는 AI 시스템입니다. "
            "위험 등급 자동 분류, 행동 가이드, AI 음성 안내 기능을 탑재하였으며 "
            "Streamlit Cloud를 통해 모바일 웹으로 배포하였습니다."
        ),
        "tags": ["Python", "XGBoost", "Streamlit", "Pandas", "공공데이터"],
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
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown(f"## {NAME}")
    st.caption(TITLE)
    st.write(BIO)

    st.markdown("---")
    st.markdown(f"[GitHub]({GITHUB_URL})")
    st.markdown(f"[LinkedIn]({LINKEDIN_URL})")
    if RESUME_URL:
        st.markdown(f"[이력서 (PDF)]({RESUME_URL})")

    st.markdown("---")
    page = st.radio("메뉴", ["소개", "프로젝트", "자격증"], label_visibility="collapsed")

# ---------------------------------------------------------------------------
# PAGE: 소개
# ---------------------------------------------------------------------------
if page == "소개":
    st.title(f"안녕하세요, {NAME}입니다 👋")
    st.subheader(TITLE)
    st.write(BIO)

    st.markdown("### Skills")
    cols = st.columns(4)
    for i, skill in enumerate(SKILLS):
        with cols[i % 4]:
            st.markdown(f"- {skill}")

    st.markdown("### 자격증")
    for cert in CERTIFICATIONS:
        st.markdown(f"**{cert['name']}**")
        st.caption(f"{cert['issuer']} {('| ' + cert['date']) if cert['date'] else ''}")
        st.markdown("---")

# ---------------------------------------------------------------------------
# PAGE: 프로젝트
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
# PAGE: 자격증
# ---------------------------------------------------------------------------
elif page == "자격증":
    st.title("자격증")
    st.write("취득한 자격증 목록입니다.")

    for cert in CERTIFICATIONS:
        st.markdown(f"**{cert['name']}**")
        st.caption(f"{cert['issuer']} {('| ' + cert['date']) if cert['date'] else ''}")
        st.markdown("---")
