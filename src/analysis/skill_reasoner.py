from src.analysis.skill_ontology import SKILL_ONTOLOGY, build_reverse_ontology

REVERSE_ONTOLOGY = build_reverse_ontology(SKILL_ONTOLOGY)

def reason_about_skill(resume_skill, jd_skill, semantic_evidence, semantic_threshold=0.6):
    resume_set = set(resume_skill)

    reasoning = {}
    matched_count = 0
    partial_count = 0

    for jd_sk in jd_skill:

        if jd_sk in resume_set:
            reasoning[jd_sk] = {
                "status": "matched",
                "evidence": "Exact skill found in resume",
                "confidence": 1.0
            }
            matched_count += 1
            continue

        # Check if JD skill is a child of any parent that the resume has
        parents = REVERSE_ONTOLOGY.get(jd_sk, set())
        parent_overlap = parents.intersection(resume_set)

        if parent_overlap:
            reasoning[jd_sk] = {
                "status": "partial",
                "evidence": f"Parent skill found in resume: {list(parent_overlap)}",
                "confidence": 0.7
            }
            partial_count += 1
            continue

        # Check if resume has sub-skills of the JD skill
        subs = SKILL_ONTOLOGY.get(jd_sk, set())
        overlap = subs.intersection(resume_set)

        if overlap:
            reasoning[jd_sk] = {
                "status": "partial",
                "evidence": f"Related sub-skills found: {list(overlap)}",
                "confidence": 0.7
            }
            partial_count += 1
            continue

        if jd_sk in semantic_evidence:
            best_skill, best_score = max(
                semantic_evidence[jd_sk],
                key=lambda x: x[1]
            )

            if best_score >= semantic_threshold:
                reasoning[jd_sk] = {
                    "status": "partial",
                    "evidence": f"Semantically related skill: {best_skill}",
                    "confidence": round(best_score, 2)
                }
                partial_count += 1
                continue

        reasoning[jd_sk] = {
            "status": "missing",
            "evidence": "No supporting evidence found",
            "confidence": 0.0
        }

    coverage = int(
        (matched_count + 0.5 * partial_count) / len(jd_skill) * 100
    )

    return {
        "skills": reasoning,
        "summary": {
            "matched": matched_count,
            "partial": partial_count,
            "missing": len(jd_skill) - matched_count - partial_count,
            "coverage": coverage
        }
    }
