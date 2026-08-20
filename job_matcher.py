import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_roles(job_file="data/job_roles.csv"):
    """Load job roles and their required skills."""
    return pd.read_csv(job_file)


def calculate_match_scores(resume_text, job_file="data/job_roles.csv"):
    """
    Calculate job-role match scores using:
    70% skill overlap
    30% TF-IDF cosine similarity
    """

    jobs_df = load_job_roles(job_file)

    job_texts = jobs_df["Required Skills"].tolist()

    # -----------------------------------------
    # TF-IDF SIMILARITY
    # -----------------------------------------

    documents = [resume_text] + job_texts

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    resume_vector = vectors[0]
    job_vectors = vectors[1:]

    similarities = cosine_similarity(
        resume_vector,
        job_vectors
    )[0]


    # -----------------------------------------
    # CALCULATE FINAL SCORES
    # -----------------------------------------

    results = []

    resume_text_lower = resume_text.lower()

    for i, similarity_score in enumerate(similarities):

        required_skills_text = jobs_df.iloc[i]["Required Skills"]

        required_skills = [
            skill.strip()
            for skill in required_skills_text.split(",")
        ]

        matched_skills = []

        for skill in required_skills:

            if skill.lower() in resume_text_lower:
                matched_skills.append(skill)


        # Skill overlap percentage
        if required_skills:

            skill_score = (
                len(matched_skills) /
                len(required_skills)
            )

        else:

            skill_score = 0


        # Final weighted score
        final_score = (
            (skill_score * 0.70) +
            (similarity_score * 0.30)
        )


        results.append({
            "Job Role": jobs_df.iloc[i]["Job Role"],
            "Match Score": round(final_score * 100, 2)
        })


    # Sort highest match first
    results = sorted(
        results,
        key=lambda x: x["Match Score"],
        reverse=True
    )

    return results