import re

DEGREE_PATTERNS = {
    # Doctorate
    "PhD": [
        r"\bph\.?d\.?\b",
        r"\bdoctor of philosophy\b"
    ],

    # Master's
    "MBA": [
        r"\bmba\b",
        r"\bmaster of business administration\b"
    ],
    "M.Tech": [
        r"\bm\.?tech\b",
        r"\bmaster of technology\b"
    ],
    "M.E.": [
        r"\bm\.?e\.?\b",
        r"\bmaster of engineering\b"
    ],
    "M.S.": [
        r"\bm\.?s\.?\b",
        r"\bmaster of science\b"
    ],
    "MCA": [
        r"\bmca\b",
        r"\bmaster of computer applications\b"
    ],
    "M.Sc": [
        r"\bm\.?sc\b",
        r"\bmaster of science\b"
    ],
    "M.Com": [
        r"\bm\.?com\b",
        r"\bmaster of commerce\b"
    ],
    "M.A.": [
        r"\bm\.?a\.?\b",
        r"\bmaster of arts\b"
    ],

    # Bachelor's
    "B.Tech": [
        r"\bb\.?tech\b",
        r"\bbachelor of technology\b"
    ],
    "B.E.": [
        r"\bb\.?e\.?\b",
        r"\bbachelor of engineering\b"
    ],
    "BCA": [
        r"\bbca\b",
        r"\bbachelor of computer applications\b"
    ],
    "B.Sc": [
        r"\bb\.?sc\b",
        r"\bbachelor of science\b"
    ],
    "B.Com": [
        r"\bb\.?com\b",
        r"\bbachelor of commerce\b"
    ],
    "B.A.": [
        r"\bb\.?a\.?\b",
        r"\bbachelor of arts\b"
    ],
    "LLB": [
        r"\bllb\b",
        r"\bbachelor of laws\b"
    ],
    "BBA": [
        r"\bbba\b",
        r"\bbachelor of business administration\b"
    ],
    "B.Pharm": [
        r"\bb\.?pharm\b",
        r"\bbachelor of pharmacy\b"
    ],
    "BDS": [
        r"\bbds\b",
        r"\bbachelor of dental surgery\b"
    ],
    "MBBS": [
        r"\bmbbs\b",
        r"\bbachelor of medicine\b"
    ],
    "B.Arch": [
        r"\bb\.?arch\b",
        r"\bbachelor of architecture\b"
    ],

    # Diplomas
    "Diploma": [
        r"\bdiploma\b",
        r"\bpolytechnic\b"
    ],

    # School
    "12th": [
        r"\b12th\b",
        r"\bintermediate\b",
        r"\bhigher secondary\b",
        r"\bhsc\b"
    ],
    "10th": [
        r"\b10th\b",
        r"\bmatric\b",
        r"\bsecondary school\b",
        r"\bssc\b"
    ]
}


def extract_education(text):
    """
    Extract education degrees from resume text.
    """
    text = text.lower()

    education = []

    for degree, patterns in DEGREE_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, text):
                education.append(degree)
                break

    return sorted(set(education))


if __name__ == "__main__":
    sample = """
    Education:
    Bachelor of Technology in Computer Science
    Master of Business Administration
    Higher Secondary (12th)
    """

    print(extract_education(sample))