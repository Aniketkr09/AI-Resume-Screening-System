import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_text
from bert_matcher import ResumeMatcher
from skill_extractor import extract_skills
from skill_gap import skill_gap
from recommendation_engine import recommend
from experience_extractor import extract_experience
from education_extractor import extract_education

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# MODEL INITIALIZATION
# --------------------------------------------------

@st.cache_resource
def load_matcher():
    return ResumeMatcher()

matcher = load_matcher()

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🚀Resume Screening System")

st.markdown("""
Upload multiple resumes and compare them against a job description.
The system will rank candidates based on resume-job matching.
""")

# --------------------------------------------------
# JOB DESCRIPTION
# --------------------------------------------------

job_description = st.text_area(
    "Paste Job Description",
    height=250
)

# --------------------------------------------------
# FILE UPLOAD
# --------------------------------------------------

uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

if st.button("Analyze Candidates"):

    if not job_description.strip():
        st.error("Please enter a Job Description.")
        st.stop()

    if not uploaded_files:
        st.error("Please upload at least one resume.")
        st.stop()

    results = []
    progress_bar = st.progress(0)

    for idx, file in enumerate(uploaded_files):

        try:
            resume_text = extract_text(file)

            similarity_score = float(
                matcher.calculate_similarity(
                    resume_text,
                    job_description
                )
            )

            skills = extract_skills(resume_text)

            matched_skills, missing_skills = skill_gap(
                resume_text,
                job_description
            )

            experience = extract_experience(
                resume_text
            )

            education = extract_education(
                resume_text
            )

            recommendation = recommend(
                similarity_score
            )

            results.append({
                "Candidate": file.name,
                "Match Score": round(similarity_score, 2),
                "Experience (Years)": experience,
                "Skills Found": ", ".join(skills) if skills else "N/A",
                "Matched Skills": ", ".join(matched_skills) if matched_skills else "None",
                "Missing Skills": ", ".join(missing_skills) if missing_skills else "None",
                "Education": ", ".join(education) if education else "N/A",
                "Recommendation": recommendation
            })

        except Exception as e:
            st.warning(f"Error processing {file.name}: {str(e)}")

        progress_bar.progress((idx + 1) / len(uploaded_files))

    # --------------------------------------------------
    # RESULTS
    # --------------------------------------------------

    if results:

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="Match Score",
            ascending=False
        ).reset_index(drop=True)

        df.index += 1

        st.success("Analysis Completed Successfully!")

        # --------------------------------------------------
        # CANDIDATE TABLE
        # --------------------------------------------------

        st.subheader("🏆 Candidate Ranking")

        st.dataframe(
            df,
            use_container_width=True
        )

        # --------------------------------------------------
        # TOP CANDIDATE
        # --------------------------------------------------

        top = df.iloc[0]

        st.subheader("🥇 Top Candidate")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Candidate",
                top["Candidate"]
            )

        with col2:
            st.metric(
                "Match Score",
                f"{top['Match Score']}%"
            )

        with col3:
            st.metric(
                "Recommendation",
                top["Recommendation"]
            )

        # --------------------------------------------------
        # SCORE CHART
        # --------------------------------------------------

        st.subheader("📊 Candidate Scores")

        fig = px.bar(
            df,
            x="Candidate",
            y="Match Score",
            title="Resume Match Scores",
            text="Match Score"
        )

        fig.update_traces(
            textposition="outside"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # --------------------------------------------------
        # DETAILED REVIEW
        # --------------------------------------------------

        st.subheader("📋 Detailed Candidate Review")

        selected_candidate = st.selectbox(
            "Select Candidate",
            df["Candidate"]
        )

        row = df[
            df["Candidate"] == selected_candidate
        ].iloc[0]

        st.markdown(
            f"### {selected_candidate}"
        )

        st.write(
            f"**Match Score:** {row['Match Score']}%"
        )

        st.write(
            f"**Experience:** {row['Experience (Years)']} Years"
        )

        st.write(
            f"**Education:** {row['Education']}"
        )

        st.write(
            f"**Recommendation:** {row['Recommendation']}"
        )

        st.markdown("### ✅ Matched Skills")
        st.success(row["Matched Skills"])

        st.markdown("### ❌ Missing Skills")
        st.error(row["Missing Skills"])

    else:
        st.warning("No valid resumes were processed.")
        