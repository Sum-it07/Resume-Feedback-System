from flask import Flask,render_template,request
from src.analysis.skill_extraction import load_skill,extract_skill
from src.analysis.semantic_matcher import semantic_candidates
from src.analysis.skill_reasoner import reason_about_skill
from src.analysis.normalize_skill import normalize_skill 
from src.analysis.feedback_generator import generate_feedback

app=Flask(__name__)
SKILL_LIST=load_skill("data/skill.txt")

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        resume = request.form["resume"]
        jd = request.form["jd"]

        skill = load_skill("data/skill.txt")

        resume_skill = normalize_skill(extract_skill(resume, skill))
        jd_skill = normalize_skill(extract_skill(jd, skill))

        semantic_evidence = semantic_candidates(resume_skill, jd_skill)
        skill_match = reason_about_skill(resume_skill, jd_skill, semantic_evidence)

        feedback = generate_feedback(
            skill_match["matched"],
            skill_match["missing"],
            skill_match["coverage"]
        )

        result = {
            "resume_skill": resume_skill,
            "jd_skill": jd_skill,
            "match": skill_match,
            "feedback": feedback
        }

    return render_template("index.html", result=result)


if __name__=="__main__":
    app.run(debug=True)