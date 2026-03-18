from resume_parser import extract_resume_text, extract_skills
from job_fetcher import fetch_jobs
# resume_file = "../resume/vijay_resume.pdf"
import os
from matcher import calculate_match_score, explain_match
try:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    resume_file = os.path.join(base_dir, "cv", "Vijay_Kashyap_Resume.pdf")
# Extract resume text
    text = extract_resume_text(resume_file)

    # Extract skills
    skills = extract_skills(text)

    print("\nSkills found in resume:\n")
    for skill in skills:
        print(skill)

    # Fetch jobs
    print("\nFetching jobs...\n")
    jobs = fetch_jobs("python developer")

    print("\nTop Job Matches:\n")

    # Match jobs
    for job in jobs:
        try:
            # score = calculate_match_score(skills, job["description"])
            score = calculate_match_score(text, job["description"])
            #print(f"{job['title']} - {job['company']} → {score}% match")
            matched, missing = explain_match(skills, job["description"])

            print(f"{job['title']} - {job['company']} → {score}% match")

            print("Matched Skills:", matched)
            print("Missing Skills:", missing)
            print("-" * 50)
        except Exception as e:
            print("Error processing job:", e)

except Exception as e:
    print("Application error:", e)   