import streamlit as st
import os

from src.resume_parser import extract_resume_text, extract_skills
from src.job_fetcher import fetch_jobs
from src.matcher import calculate_match_score, explain_match

st.title("AI Resume Analyzer + Job Matcher")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    # Save uploaded file
    file_path = os.path.join("resume", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

    # Extract text and skills
    text = extract_resume_text(file_path)
    skills = extract_skills(text)

    st.subheader("Extracted Skills:")
    st.write(skills)

    # Fetch jobs
    st.spinner("Processing...")
    st.subheader("Fetching jobs...")
    jobs = fetch_jobs("developer")

    results = []
    for job in jobs:

        score = calculate_match_score(text, job["description"])
        matched, missing = explain_match(skills, job["description"])

        results.append({
            "title": job["title"],
            "company": job["company"],
            "score": score,
            "matched": matched,
            "missing": missing
        })

    

    # Sort by best match
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    st.subheader("Top Job Matches:")
    st.dataframe(results)
    for job in results:

        st.write(f"**{job['title']}** - {job['company']}")
        st.write(f"Match Score: {job['score']}%")

        st.write("Matched Skills:", job["matched"])
        st.write("Missing Skills:", job["missing"])

        st.write("---")

    
    
    
