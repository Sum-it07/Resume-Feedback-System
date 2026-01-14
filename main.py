from src.analysis.skill_extraction import load_skill,extract_skill
from pathlib import Path
def load_text(path):
    return Path(path).read_text(encoding="utf-8")

def main():
    resume=load_text("data/resume/resume1.txt")
    jd=load_text("data/job_description/jd1.txt")
    skill=load_skill("data/skill.txt")

    resume_skill=extract_skill(resume, skill)
    jd_skill=extract_skill(jd, skill)
    print("==Your Resume==")
    print(resume)

    print("==Job description==")
    print(jd)

    print("==resume skill")
    print(resume_skill)
    print("==jd skill")
    print(jd_skill)

if __name__== "__main__":
    main()

