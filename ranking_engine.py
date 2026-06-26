def final_score(
        semantic_score,
        skill_score,
        experience_score,
        education_score
):

    return round(
        semantic_score * 0.4
        + skill_score * 0.3
        + experience_score * 0.2
        + education_score * 0.1,
        2
    )