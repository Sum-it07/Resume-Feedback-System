def generate_feedback(reasoning_result):
    feedback = []

    summary = reasoning_result["summary"]
    skills = reasoning_result["skills"]

    coverage = summary["coverage"]

    # Overall assessment
    if coverage >= 80:
        feedback.append(
            f"Your resume shows strong alignment with the role, matching {coverage}% of the required skills."
        )
    elif coverage >= 50:
        feedback.append(
            f"Your resume shows moderate alignment with the role, matching {coverage}% of the required skills."
        )
    else:
        feedback.append(
            f"Your resume currently matches only {coverage}% of the required skills and needs improvement."
        )

    # Strengths
    matched = [
        skill for skill, info in skills.items()
        if info["status"] == "matched"
    ]

    if matched:
        feedback.append(
            "Strong evidence found for the following required skills: "
            + ", ".join(matched)
        )

    # Partial matches (important for AI lab)
    partial = {
        skill: info for skill, info in skills.items()
        if info["status"] == "partial"
    }

    if partial:
        lines = []
        for skill, info in partial.items():
            lines.append(
                f"{skill} (confidence: {info['confidence']}, reason: {info['evidence']})"
            )

        feedback.append(
            "Some skills are partially satisfied based on related experience: "
            + "; ".join(lines)
        )

    # Missing skills
    missing = [
        skill for skill, info in skills.items()
        if info["status"] == "missing"
    ]

    if missing:
        feedback.append(
            "To improve your fit for the role, consider adding or strengthening the following skills: "
            + ", ".join(missing)
        )

    return "\n".join(feedback)
