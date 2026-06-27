def extract_skills(text):

    skills_database = [

        "python",
        "java",
        "c++",
        "machine learning",
        "deep learning",
        "artificial intelligence",
        "data science",
        "sql",
        "mongodb",
        "tensorflow",
        "pytorch",
        "keras",
        "flask",
        "django",
        "html",
        "css",
        "javascript",
        "react",
        "git",
        "docker",
        "aws",
        "nlp",
        "computer vision"

    ]


    found_skills = []


    for skill in skills_database:

        if skill.lower() in text.lower():

            found_skills.append(skill)


    return found_skills



def find_missing_skills(resume_text, job_text):


    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_text)


    missing = []


    for skill in job_skills:

        if skill not in resume_skills:

            missing.append(skill)


    return missing