from flask import Flask, render_template, request
from src.analysis.skill_extraction import load_skill, extract_skill
from src.analysis.semantic_matcher import semantic_candidates
from src.analysis.skill_reasoner import reason_about_skill
from src.analysis.normalize_skill import normalize_skill
from src.analysis.feedback_generator import generate_feedback
from src.analysis.document_loader import load_document
from pathlib import Path

app = Flask(__name__)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

SKILL_LIST = load_skill("data/skill.txt")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        resume_file = request.files.get("resume_file")
        jd_file = request.files.get("jd_file")

        if not resume_file or not jd_file:
            return render_template("index.html", result=None)

        resume_path = UPLOAD_DIR / resume_file.filename
        jd_path = UPLOAD_DIR / jd_file.filename

        resume_file.save(resume_path)
        jd_file.save(jd_path)

        resume_text = load_document(resume_path)
        jd_text = load_document(jd_path)

        resume_skill = normalize_skill(
            extract_skill(resume_text, SKILL_LIST)
        )
        jd_skill = normalize_skill(
            extract_skill(jd_text, SKILL_LIST)
        )

        semantic_evidence = semantic_candidates(resume_skill, jd_skill)
        skill_match = reason_about_skill(
            resume_skill, jd_skill, semantic_evidence
        )

        feedback = generate_feedback(skill_match)

        result = {
            "resume_skill": resume_skill,
            "jd_skill": jd_skill,
            "match": skill_match,
            "feedback": feedback
        }
        print(skill_match)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
