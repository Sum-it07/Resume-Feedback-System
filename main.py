from src.analysis.skill_extraction import load_skill,extract_skill
# from src.analysis.skill_matching import skill_matching
# from src.analysis.semantic_matcher import semantic_match
from src.analysis.semantic_matcher import semantic_candidates
from src.analysis.skill_reasoner import reason_about_skill
from src.analysis.normalize_skill import normalize_skill 
from src.analysis.feedback_generator import generate_feedback
from pathlib import Path
def load_text(path):
    return Path(path).read_text(encoding="utf-8")

def main():
    resume=load_text("data/resume/resume1.txt")
    jd=load_text("data/job_description/jd1.txt")
    skill=load_skill("data/skill.txt")


    resume_skill=extract_skill(resume, skill)
    resume_skill=normalize_skill(resume_skill)
    jd_skill=extract_skill(jd, skill)
    jd_skill=normalize_skill(jd_skill)
    print("==Your Resume==")
    print(resume)

    print("==Job description==")
    print(jd)

    print("==resume skill")
    print(resume_skill)
    print("==jd skill==")
    print(jd_skill)

    print("== skill matched ==")
    semantic_evidance=semantic_candidates(resume_skill,jd_skill)
    skill_match=reason_about_skill(resume_skill,jd_skill,semantic_evidance)
    print(skill_match)
    print("==Feedback Time==")
    print(generate_feedback(skill_match["matched"],skill_match["missing"],skill_match["coverage"]))

if __name__== "__main__":
    main()

