SKILL_FAMILIES = {
    "c": {"c++", "c#"},
    "js": {"javascript"},
    "py": {"python"}
}

def suppress_using_families(found_skills, SKILL_FAMILIES):
    final = set(found_skills)

    for base, variants in SKILL_FAMILIES.items():
        if variants & found_skills and base in final:
                final.remove(base)

    return sorted(final)
