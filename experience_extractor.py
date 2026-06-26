import re

def extract_experience(text):

    patterns = [
        r"(\d+)\+?\s+years",
        r"(\d+)\+?\s+yrs"
    ]

    years = []

    for pattern in patterns:

        matches = re.findall(pattern, text.lower())

        years.extend(matches)

    if years:
        return max([int(x) for x in years])

    return 0