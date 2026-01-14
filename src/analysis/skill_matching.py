def skill_matching(resume_skill,required_skill):
    resume_set=set(resume_skill)
    required_set=set(required_skill)

    matched_skill=sorted(resume_set.intersection(required_set))
    missing_skill=sorted(required_set - resume_set)
    coverage=int((len(matched_skill)/len(required_set))*100)
    return {
        "matched":matched_skill,
        "missing":missing_skill,
        "coverage":coverage
    }