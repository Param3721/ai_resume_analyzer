import streamlit as st

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import extract_skills
from job_matcher import calculate_match_scores
from roadmap_generator import generate_skill_gap, generate_roadmap


# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("📄 Resume Analyzer")

st.sidebar.write(
    "Analyze your resume, discover suitable job roles, "
    "identify skill gaps, and create a learning roadmap."
)

st.sidebar.markdown("---")

st.sidebar.write("### Project Features")

st.sidebar.write("✅ Resume Text Extraction")
st.sidebar.write("✅ Skill Detection")
st.sidebar.write("✅ Job Role Matching")
st.sidebar.write("✅ Skill Gap Analysis")
st.sidebar.write("✅ Learning Roadmap")


# -------------------------------------------------
# MAIN PAGE
# -------------------------------------------------

st.title("📄 AI Resume Analyzer & Job Recommendation System")

st.write(
    "Upload your resume to analyze your skills, "
    "compare them with job roles, and identify skill gaps."
)

st.markdown("---")


# -------------------------------------------------
# RESUME UPLOAD
# -------------------------------------------------

st.header("1. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)",
    type=["pdf", "docx"]
)


if uploaded_file is not None:

    st.success(f"✅ Uploaded: {uploaded_file.name}")

    try:

        # -----------------------------------------
        # EXTRACT RESUME TEXT
        # -----------------------------------------

        resume_text = extract_resume_text(uploaded_file)

        if resume_text.strip():

            st.subheader("📄 Extracted Resume Text")

            st.text_area(
                "Resume Content",
                resume_text,
                height=250
            )


            # -----------------------------------------
            # CLEAN TEXT
            # -----------------------------------------

            cleaned_text = clean_text(resume_text)


            # -----------------------------------------
            # SKILL EXTRACTION
            # -----------------------------------------

            detected_skills = extract_skills(cleaned_text)

            st.markdown("---")

            st.header("2. Detected Skills")

            if detected_skills:

                st.write(
                    f"We found **{len(detected_skills)} skills** "
                    "in your resume."
                )

                st.write(", ".join(detected_skills))

            else:

                st.warning(
                    "No matching skills were found in the resume."
                )


            # -----------------------------------------
            # JOB ROLE RECOMMENDATIONS
            # -----------------------------------------

            st.markdown("---")

            st.header("3. Job Role Recommendations")

            match_results = calculate_match_scores(cleaned_text)

            if match_results:

                st.write("### Top 3 Recommended Roles")

                for index, result in enumerate(
                    match_results[:3],
                    start=1
                ):

                    role = result["Job Role"]
                    score = result["Match Score"]

                    st.write(
                        f"**{index}. {role} — {score}% Match**"
                    )

                    st.progress(score / 100)

            else:

                st.warning(
                    "No suitable job-role matches were found."
                )


            # -----------------------------------------
            # TARGET ROLE
            # -----------------------------------------

            st.markdown("---")

            st.header("4. Target Role Skill Gap Analysis")

            target_role = st.selectbox(
                "Select your target job role",
                [
                    "Data Analyst",
                    "Machine Learning Engineer",
                    "AI Engineer",
                    "NLP Engineer",
                    "Computer Vision Engineer"
                ]
            )


            # -----------------------------------------
            # SKILL GAP ANALYSIS
            # -----------------------------------------

            found_skills, missing_skills = generate_skill_gap(
                detected_skills,
                target_role
            )

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("✅ Skills Found")

                if found_skills:

                    for skill in found_skills:
                        st.write(f"✅ {skill}")

                else:

                    st.info(
                        "No required skills for this role "
                        "were detected."
                    )


            with col2:

                st.subheader("❌ Missing Skills")

                if missing_skills:

                    for skill in missing_skills:
                        st.write(f"❌ {skill}")

                else:

                    st.success(
                        "No missing skills for this role!"
                    )


            # -----------------------------------------
            # LEARNING ROADMAP
            # -----------------------------------------

            st.markdown("---")

            st.header("5. Learning Roadmap")

            if missing_skills:

                roadmap = generate_roadmap(missing_skills)

                for item in roadmap:

                    st.write(
                        f"**{item['Week']} — {item['Topic']}**"
                    )

                    st.write(
                        f"🎯 {item['Goal']}"
                    )

            else:

                st.success(
                    "🎉 You already have all the required "
                    "skills for this role!"
                )


        else:

            st.warning(
                "No text could be extracted from this resume."
            )


    except Exception as e:

        st.error(
            f"An error occurred while analyzing the resume: {e}"
        )


else:

    st.info(
        "👆 Upload a PDF or DOCX resume to begin the analysis."
    )