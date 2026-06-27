from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model once (important for performance)
model = SentenceTransformer('all-MiniLM-L6-v2')


def calculate_match(resume, job, resume_skills, job_skills):

    # -----------------------------
    # SEMANTIC TEXT MATCH (BERT)
    # -----------------------------
    embeddings = model.encode([resume, job])

    text_score = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0] * 100


    # -----------------------------
    # SKILL MATCHING
    # -----------------------------
    resume_set = set([s.lower() for s in resume_skills])

    matched = 0

    for skill in job_skills:
        if skill.lower() in resume_set:
            matched += 1


    skill_score = (
        matched / len(job_skills)
        if job_skills else 0
    ) * 100


    # -----------------------------
    # FINAL SCORE (IMPROVED WEIGHT)
    # -----------------------------
    final_score = (
        text_score * 0.4 +
        skill_score * 0.6
    )


    return round(final_score, 2)