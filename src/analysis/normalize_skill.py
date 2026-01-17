ALIASES = {
    "ml": "machine learning",
    "dl": "deep learning",
    "ai": "artificial intelligence",
    "nlp": "natural language processing"
}

def normalize_skill(skills):
    return sorted({
        ALIASES.get(skill.lower(), skill.lower())
        for skill in skills
    })
