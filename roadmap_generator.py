import pandas as pd


def generate_skill_gap(resume_skills, target_role, job_file="data/job_roles.csv"):
    """Find skills that are present and missing for a target role."""

    jobs_df = pd.read_csv(job_file)

    role_data = jobs_df[
        jobs_df["Job Role"].str.lower() == target_role.lower()
    ]

    if role_data.empty:
        return [], []

    required_skills = [
        skill.strip()
        for skill in role_data.iloc[0]["Required Skills"].split(",")
    ]

    resume_skills_lower = [skill.lower() for skill in resume_skills]

    found_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill.lower() in resume_skills_lower:
            found_skills.append(skill)
        else:
            missing_skills.append(skill)

    return found_skills, missing_skills


def generate_roadmap(missing_skills):
    """Create a simple learning roadmap."""

    roadmap = []

    for week, skill in enumerate(missing_skills, start=1):
        roadmap.append({
            "Week": f"Week {week}",
            "Topic": skill,
            "Goal": f"Learn the basics of {skill}"
        })

    return roadmap