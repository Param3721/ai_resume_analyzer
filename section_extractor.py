import re


def extract_sections(text):
    """
    Extract common resume sections using simple heading-based matching.
    """

    sections = {
        "Education": "",
        "Experience": "",
        "Projects": ""
    }

    cleaned_text = text.replace("\r", "\n")

    patterns = {
        "Education": r"(education|academic background)",
        "Experience": r"(experience|work experience|professional experience)",
        "Projects": r"(projects|academic projects|personal projects)"
    }

    section_positions = []

    for section_name, pattern in patterns.items():
        match = re.search(
            rf"(?im)^\s*{pattern}\s*:?\s*$",
            cleaned_text
        )

        if match:
            section_positions.append(
                (match.start(), match.end(), section_name)
            )

    section_positions.sort()

    for i, (_, start_content, section_name) in enumerate(section_positions):

        if i + 1 < len(section_positions):
            end_content = section_positions[i + 1][0]
        else:
            end_content = len(cleaned_text)

        section_text = cleaned_text[
            start_content:end_content
        ].strip()

        sections[section_name] = section_text

    return sections