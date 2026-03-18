from sentence_transformers import SentenceTransformer, util

# Load model once (important)
model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_match_score(resume_text, job_description):

    try:
        # Convert text to embeddings
        resume_embedding = model.encode(resume_text, convert_to_tensor=True)
        job_embedding = model.encode(job_description, convert_to_tensor=True)

        # Compute similarity
        similarity = util.cos_sim(resume_embedding, job_embedding)

        score = float(similarity[0][0]) * 100

        return round(score, 2)

    except Exception as e:
        print("AI Matching Error:", e)
        return 0
def explain_match(resume_skills, job_description):

    job_description = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in resume_skills:
        if skill in job_description:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills    