def generate_feedback(resume_skills, missing_skills, score):

    feedback = []


    # -------------------------
    # SCORE ANALYSIS
    # -------------------------
    if score >= 85:
        feedback.append(
            "Strong candidate profile for this role."
        )

    elif score >= 70:
        feedback.append(
            "Good match. Minor improvements recommended."
        )

    else:
        feedback.append(
            "Candidate needs significant improvement for this role."
        )


    # -------------------------
    # SKILL GAP ANALYSIS
    # -------------------------
    if missing_skills:

        feedback.append(
            "Skill Gap Identified: " + ", ".join(missing_skills)
        )

        feedback.append(
            "Recommended Actions: "
            "Work on missing skills through projects, certifications, and real-world practice."
        )

    else:

        feedback.append(
            "No major skill gaps detected."
        )


    # -------------------------
    # RESUME IMPROVEMENT TIPS
    # -------------------------
    feedback.append("Resume Optimization Tips:")

    feedback.append("• Add measurable project outcomes (accuracy, performance)")
    feedback.append("• Mention deployment tools (Docker, APIs, Cloud)")
    feedback.append("• Highlight end-to-end project workflow")
    feedback.append("• Include datasets and model details")


    return feedback