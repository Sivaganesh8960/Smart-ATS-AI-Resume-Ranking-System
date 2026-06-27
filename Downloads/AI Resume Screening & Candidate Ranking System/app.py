from flask import Flask, render_template, request
import os

from models.matcher import calculate_match

from utils.pdf_reader import extract_text
from utils.text_cleaner import clean_text

from utils.skill_extractor import (
    extract_skills,
    find_missing_skills
)

from utils.feedback_generator import generate_feedback


from database.db import (
    create_database,
    save_candidate
)



app = Flask(__name__)


UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


create_database()



@app.route("/")
def home():

    return render_template("index.html")




@app.route("/upload", methods=["POST"])
def upload_resume():


    file = request.files.get("resume")


    if not file or file.filename == "":

        return "Please upload resume"



    path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )


    file.save(path)



    resume_text = extract_text(path)


    if not resume_text:

        return "Could not read PDF"



    cleaned_resume = clean_text(
        resume_text
    )


    resume_skills = extract_skills(
        cleaned_resume
    )



    job_text = request.form.get(
        "job_text"
    )


    job_file = request.files.get(
        "job_file"
    )



    job_description = None



    if job_file and job_file.filename:


        job_path = os.path.join(
            UPLOAD_FOLDER,
            job_file.filename
        )


        job_file.save(job_path)


        job_description = extract_text(
            job_path
        )


    elif job_text:

        job_description = job_text





    score = None

    missing = []

    feedback = []




    if job_description:


        cleaned_job = clean_text(
            job_description
        )


        job_skills = extract_skills(
            cleaned_job
        )



        score = calculate_match(
            cleaned_resume,
            cleaned_job,
            resume_skills,
            job_skills
        )



        missing = find_missing_skills(
            cleaned_resume,
            cleaned_job
        )



        feedback = generate_feedback(
            resume_skills,
            missing,
            score
        )



        save_candidate(
            file.filename,
            resume_skills,
            score,
            missing
        )


    else:


        feedback = [
            "Upload a job description to generate suggestions."
        ]



    return render_template(
        "result.html",
        skills=resume_skills,
        score=score,
        missing=missing,
        feedback=feedback
    )





@app.route("/rank", methods=["POST"])
def rank_candidates():


    job = request.form.get(
        "job_text"
    )


    if not job:

        return "Job description required"



    cleaned_job = clean_text(job)


    job_skills = extract_skills(
        cleaned_job
    )



    resumes = request.files.getlist(
        "resumes"
    )



    candidates = []



    for resume in resumes:


        path = os.path.join(
            UPLOAD_FOLDER,
            resume.filename
        )


        resume.save(path)



        text = extract_text(path)



        if not text:

            continue



        cleaned = clean_text(text)



        skills = extract_skills(
            cleaned
        )



        score = calculate_match(
            cleaned,
            cleaned_job,
            skills,
            job_skills
        )



        missing = find_missing_skills(
            cleaned,
            cleaned_job
        )



        feedback = generate_feedback(
            skills,
            missing,
            score
        )



        save_candidate(
            resume.filename,
            skills,
            score,
            missing
        )



        candidates.append(
            {
                "name": resume.filename,
                "score": score,
                "skills": skills,
                "missing": missing,
                "feedback": feedback
            }
        )



    candidates = sorted(
        candidates,
        key=lambda x:x["score"],
        reverse=True
    )



    return render_template(
        "dashboard.html",
        candidates=candidates
    )





if __name__ == "__main__":

    app.run(debug=True)