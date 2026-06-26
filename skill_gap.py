from skill_extractor import extract_skills

def skill_gap(
        resume_text,
        job_description
):

    resume_skills = set(
        extract_skills(resume_text)
    )

    jd_skills = set(
        extract_skills(job_description)
    )

    matched = list(
        resume_skills.intersection(jd_skills)
    )

    missing = list(
        jd_skills - resume_skills
    )

    return matched, missing