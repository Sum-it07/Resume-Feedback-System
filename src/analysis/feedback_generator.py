# from src.analysis.skill_matching import skill_matching

def generate_feedback(matched,missing,coverage):
    feedback=[]
    if(coverage>80):
        feedback.append("You resume shows strong alignment with the role, mactching "+str(coverage)+"% of skills.")

    elif(coverage>=50):
        feedback.append("Your resume shows moderate alignment with the role, matching "+str(coverage)+ "% of the required skills.")
    else:
        feedback.append("Your resume currently matches only " + str(coverage)+ "% of the required skills and need improvement.")

    #strength
    if matched:
        skill=",".join(matched)
        feedback.append("Relevant skills intentified in your resume includes "+skill)

    #weakness
    if missing:
        skill=",".join(missing)
        feedback.append("To improve your fit for the role, consider adding or stengthening the following skills: "+skill)
    return "\n".join(feedback)