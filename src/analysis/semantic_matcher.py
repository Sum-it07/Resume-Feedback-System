from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def semantic_candidates(resume_skill,required_skill,threshold=0.7):
    resume_emb=model.encode(resume_skill)
    required_emb=model.encode(required_skill)
    similarity=cosine_similarity(required_emb,resume_emb)

    evidence = {}

    for i, required_skill in enumerate(required_skill):
        j = similarity[i].argmax()
        score = similarity[i][j]

        if score >= threshold:
            evidence[required_skill] = {
                "resume_skill": resume_skill[j],
                "score": round(float(score), 2)
            }

    return evidence



# def semantic_match(resume_skill,required_skill,threshold=0.7):
#     resume_emb=model.encode(resume_skill)
#     required_emb=model.encode(required_skill)
#     similarity=cosine_similarity(required_emb,resume_emb)

    # matched=[]
    # missing=[]

    # for i,skill in enumerate(required_skill):
    #     max_score= similarity[i].max()
    #     if max_score>=threshold:
    #         matched.append(skill)
    #     else:
    #         missing.append(skill)
    
    # coverage=int((len(matched)/len(required_skill))*100)

    # return {
    #     "matched":matched,
    #     "missing":missing,
    #     "coverage":coverage
    # }

