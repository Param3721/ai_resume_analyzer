import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_job_roles(job_file="data/job_roles.csv"):
    """Load job roles and their required skills."""
    return pd.read_csv(job_file)


def calculate_match_scores(resume_text, job_file="data/job_roles.csv"):
    """Calculate resume-to-job-role similarity scores."""

    jobs_df = load_job_roles(job_file)

    job_texts = jobs_df["Required Skills"].tolist()

    documents = [resume_text] + job_texts

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    resume_vector = vectors[0]
    job_vectors = vectors[1:]

    similarities = cosine_similarity(resume_vector, job_vectors)[0]

    results = []

    for i, score in enumerate(similarities):
        results.append({
            "Job Role": jobs_df.iloc[i]["Job Role"],
            "Match Score": round(score * 100, 2)
        })

    results = sorted(
        results,
        key=lambda x: x["Match Score"],
        reverse=True
    )

    return results