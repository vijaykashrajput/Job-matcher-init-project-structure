from pdfminer.high_level import extract_text

def extract_resume_text(file_path):

    text = extract_text(file_path)

    return text


def extract_skills(text):

    skills = [
        "python",
        "azure",
        "aws",
        "sql",
        "machine learning",
        "data engineering",
        "power bi",
        "pandas",
        "numpy",
        "django",
        "api",
        "docker"
    ]

    found_skills = []

    text = text.lower()

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills