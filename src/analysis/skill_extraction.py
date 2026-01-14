import re
from src.analysis.skill_aliases import suppress_using_families

SKILL_FAMILIES = {
    "c": {"c++", "c#"},
    "js": {"javascript"},
    "py": {"python"},
}

def load_skill(path):
    with open(path,"r",encoding="utf-8") as f:
        return [line.strip().lower() for line in f if line.strip()]
    

def extract_skill(text,skill_list):
    text=text.lower()
    found_skill=set()

    for skill in skill_list:
        skill=skill.lower()
        if " " in skill:
            if skill in text:
                found_skill.add(skill)
        elif re.search(r"[^a-z0-9]",skill):
            if skill in text:
                found_skill.add(skill)
        else:
            pattern=r"\b"+ re.escape(skill)+ r"\b"
            if re.search(pattern,text):
                found_skill.add(skill)
    
    return suppress_using_families(found_skill,SKILL_FAMILIES)
