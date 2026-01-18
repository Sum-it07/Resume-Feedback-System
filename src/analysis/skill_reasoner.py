from src.analysis.skill_ontology import SKILL_ONTOLOGY
def reason_about_skill(resume_skill,jd_skill,semantic_evidence):
    matched=[]
    partial={}
    missing=[]

    resume_set=set(resume_skill)
    for jd_sk in jd_skill:
        if jd_sk in resume_set:
            matched.append(jd_sk)
            continue

        subs=SKILL_ONTOLOGY.get(jd_sk,set())
        overlap=subs.intersection(resume_set)
        if overlap:
            partial[jd_sk]=list(overlap)
            continue
        
        if jd_sk in semantic_evidence:
            partial[jd_sk]=[
                f"{s} (semantic)"
                for s,_ in semantic_evidence[jd_sk]
            ]
            continue

        missing.append(jd_sk)
    
    coverage=int( (len(matched)+ 0.5*len(partial))/ len(jd_skill) *100 )

    return {
        "matched":matched,
        "partial":partial,
        "missing": missing,
        "coverage": coverage
    }