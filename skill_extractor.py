import re

SKILLS = {

    # ===========================
    # Programming Languages
    # ===========================
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "php", "ruby", "go", "rust", "kotlin", "swift", "r", "matlab",

    # ===========================
    # Web Development
    # ===========================
    "html", "css", "bootstrap", "tailwind css",
    "react", "angular", "vue", "node.js", "express.js",
    "django", "flask", "fastapi", "spring boot",

    # ===========================
    # Databases
    # ===========================
    "sql", "mysql", "postgresql", "oracle",
    "mongodb", "sqlite", "redis", "firebase",

    # ===========================
    # Data Science & AI
    # ===========================
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "data analysis",
    "nlp",
    "computer vision",
    "generative ai",
    "llm",
    "tensorflow",
    "pytorch",
    "keras",
    "scikit-learn",
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",
    "plotly",

    # ===========================
    # Cloud & DevOps
    # ===========================
    "aws", "azure", "google cloud", "docker",
    "kubernetes", "jenkins", "terraform",
    "ansible", "git", "github",

    # ===========================
    # Cybersecurity
    # ===========================
    "ethical hacking",
    "penetration testing",
    "network security",
    "cryptography",
    "wireshark",
    "kali linux",

    # ===========================
    # Networking
    # ===========================
    "tcp/ip",
    "dns",
    "dhcp",
    "routing",
    "switching",
    "ccna",

    # ===========================
    # Mobile Development
    # ===========================
    "android",
    "ios",
    "flutter",
    "react native",

    # ===========================
    # Software Testing
    # ===========================
    "manual testing",
    "automation testing",
    "selenium",
    "junit",
    "pytest",
    "testng",

    # ===========================
    # Mechanical Engineering
    # ===========================
    "autocad",
    "solidworks",
    "catia",
    "ansys",
    "manufacturing",
    "cnc",
    "thermodynamics",

    # ===========================
    # Civil Engineering
    # ===========================
    "staad pro",
    "etabs",
    "revit",
    "surveying",
    "autocad civil",
    "construction management",

    # ===========================
    # Electrical Engineering
    # ===========================
    "matlab",
    "pspice",
    "power systems",
    "control systems",
    "embedded systems",

    # ===========================
    # Electronics
    # ===========================
    "vlsi",
    "verilog",
    "fpga",
    "arduino",
    "raspberry pi",

    # ===========================
    # Business & Management
    # ===========================
    "project management",
    "business analysis",
    "agile",
    "scrum",
    "jira",
    "erp",
    "sap",

    # ===========================
    # Finance
    # ===========================
    "financial analysis",
    "accounting",
    "bookkeeping",
    "excel",
    "power bi",
    "tableau",

    # ===========================
    # Marketing
    # ===========================
    "seo",
    "sem",
    "content marketing",
    "email marketing",
    "google analytics",
    "social media marketing",

    # ===========================
    # Human Resources
    # ===========================
    "recruitment",
    "talent acquisition",
    "payroll",
    "employee engagement",

    # ===========================
    # Healthcare
    # ===========================
    "clinical research",
    "medical coding",
    "ehr",
    "patient care",

    # ===========================
    # Soft Skills
    # ===========================
    "communication",
    "leadership",
    "teamwork",
    "problem solving",
    "critical thinking",
    "time management",
    "adaptability",
    "creativity",
    "decision making",
    "presentation",


  # ======================================================
    # EDUCATION KEYWORDS (Optional)
    # ======================================================

    # School
    "10th",
    "ssc",
    "secondary school",
    "matric",

    "12th",
    "hsc",
    "higher secondary",
    "intermediate",

    # Diploma
    "diploma",
    "polytechnic",

    # Bachelor's
    "b.tech",
    "bachelor of technology",

    "b.e",
    "bachelor of engineering",

    "bca",
    "bachelor of computer applications",

    "b.sc",
    "bachelor of science",

    "b.com",
    "bachelor of commerce",

    "b.a",
    "bachelor of arts",

    "bba",
    "bachelor of business administration",

    "llb",
    "bachelor of laws",

    "b.pharm",
    "bachelor of pharmacy",

    "b.arch",
    "bachelor of architecture",

    "mbbs",
    "bachelor of medicine",

    "bds",
    "bachelor of dental surgery",

    # Master's
    "mba",
    "master of business administration",

    "m.tech",
    "master of technology",

    "m.e",
    "master of engineering",

    "mca",
    "master of computer applications",

    "m.sc",
    "master of science",

    "m.com",
    "master of commerce",

    "m.a",
    "master of arts",

    "m.pharm",
    "master of pharmacy",

    "m.arch",
    "master of architecture",

    "llm",
    "master of laws",

    "m.ed",
    "master of education",

    "msw",
    "master of social work",

    # Doctorate
    "phd",
    "ph.d",
    "doctor of philosophy",

    "postdoc",
    "post doctorate"
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s\+\#\-\.]", " ", text)
    return re.sub(r"\s+", " ", text)


def extract_skills(text):
    text = clean_text(text)

    extracted = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill) + r"\b"

        # Special cases
        if skill == "c++":
            pattern = r"c\+\+"
        elif skill == "c#":
            pattern = r"c#"
        elif skill == "node.js":
            pattern = r"node\.?js"
        elif skill == "express.js":
            pattern = r"express\.?js"

        if re.search(pattern, text):
            extracted.append(skill)

    return sorted(set(extracted))


if __name__ == "__main__":
    sample = """
    Python, SQL, Docker, AWS, TensorFlow, React,
    Leadership, Project Management, Tableau, Power BI,
    AutoCAD, SolidWorks, Communication Skills
    """

    print(extract_skills(sample))