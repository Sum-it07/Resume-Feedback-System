ALIASES = {
    "ml": "machine learning",
    "machine learning":"machine learning",
    "dl": "deep learning",
    "ai": "artificial intelligence",
    "nlp": "nlp",
    "natural language processing":"nlp"
}

def normalize_skill(skills):
    return sorted({
        ALIASES.get(skill.lower(), skill.lower())
        for skill in skills
    })
