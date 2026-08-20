import pandas as pd


def load_skills(skill_file="data/skill_dictionary.csv"):
    """Load the skill dictionary from the CSV file."""
    df = pd.read_csv(skill_file)
    return df


def extract_skills(text, skill_file="data/skill_dictionary.csv"):
    """Find skills from the resume text."""

    skills_df = load_skills(skill_file)

    found_skills = []

    for skill in skills_df["Skill"]:
        skill_lower = skill.lower()

        if skill_lower in text:
            found_skills.append(skill)

    return found_skills