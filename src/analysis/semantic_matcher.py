from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_candidates(
    resume_skill,
    required_skill,
    threshold=0.6,
    top_k=3
):
    resume_emb = model.encode(resume_skill)
    required_emb = model.encode(required_skill)

    similarity = cosine_similarity(required_emb, resume_emb)

    evidence = {}

    for i, jd_skill in enumerate(required_skill):
        scored = []

        for j, score in enumerate(similarity[i]):
            if score >= threshold:
                scored.append(
                    (resume_skill[j], round(float(score), 2))
                )

        if scored:
            # sort descending by similarity
            scored.sort(key=lambda x: x[1], reverse=True)
            evidence[jd_skill] = scored[:top_k]

    return evidence
