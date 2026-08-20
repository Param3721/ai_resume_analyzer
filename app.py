import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import calculate_match_scores
from roadmap_generator import generate_skill_gap, generate_roadmap


st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


st.title("📄 AI Resume Analyzer & Job Recommendation System")

st.write(
    "Upload your resume to analyze your skills, "
    "compare them with job roles, and identify skill gaps."
)


st.header("1. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf", "docx"]
)


if uploaded_file is not None:

    st.success(f"Uploaded: {uploaded_file.name}")

    try:
        resume_text = extract_resume_text(uploaded_file)

        if resume_text.strip():

            st.subheader("Extracted Resume Text")

            st.text_area(
                "Resume Content",
                resume_text,
                height=250
            )

            # Clean the resume text
            cleaned_text = clean_text(resume_text)

            # Extract skills
            detected_skills = extract_skills(cleaned_text)

            st.subheader("Detected Skills")

            if detected_skills:

                st.write(
                    f"We found **{len(detected_skills)} skills** "
                    "in your resume."
                )

                st.write(", ".join(detected_skills))

            else:

                st.warning("No matching skills were found.")


            # Job recommendations
            st.subheader("Job Role Recommendations")

            match_results = calculate_match_scores(cleaned_text)

            if match_results:

                st.write("### Recommended Roles")

                for index, result in enumerate(
                    match_results[:3],
                    start=1
                ):

                    st.write(
                        f"**{index}. {result['Job Role']} — "
                        f"{result['Match Score']}%**"
                    )


            # Target role
            st.subheader("Target Role Skill Gap Analysis")

            target_role = st.selectbox(
                "Select a target job role",
                [
                    "Data Analyst",
                    "Machine Learning Engineer",
                    "AI Engineer",
                    "NLP Engineer",
                    "Computer Vision Engineer"
                ]
            )


            found_skills, missing_skills = generate_skill_gap(
                detected_skills,
                target_role
            )


            col1, col2 = st.columns(2)


            with col1:

                st.write("### Skills Found")

                if found_skills:

                    for skill in found_skills:
                        st.write(f"✅ {skill}")

                else:

                    st.write("No required skills found.")


            with col2:

                st.write("### Missing Skills")

                if missing_skills:

                    for skill in missing_skills:
                        st.write(f"❌ {skill}")

                else:

                    st.write("No missing skills!")


            # Learning roadmap
            st.subheader("Learning Roadmap")

            if missing_skills:

                roadmap = generate_roadmap(missing_skills)

                for item in roadmap:

                    st.write(
                        f"**{item['Week']}** — "
                        f"{item['Topic']}: "
                        f"{item['Goal']}"
                    )

            else:

                st.success(
                    "You already have all the required skills "
                    "for this role!"
                )

        else:

            st.warning(
                "No text could be extracted from this resume."
            )


    except Exception as e:

        st.error(f"Error reading resume: {e}")
