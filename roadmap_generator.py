import pandas as pd


def generate_skill_gap(resume_skills, target_role, job_file="data/job_roles.csv"):
    """Find skills that are present and missing for a target role."""

    jobs_df = pd.read_csv(job_file)

    role_data = jobs_df[
        jobs_df["Job Role"].str.lower() == target_role.lower()
    ]

    if role_data.empty:
        return [], []

    required_skills = [
        skill.strip()
        for skill in role_data.iloc[0]["Required Skills"].split(",")
    ]

    resume_skills_lower = [
        skill.lower()
        for skill in resume_skills
    ]

    found_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in resume_skills_lower:
            found_skills.append(skill)

        else:
            missing_skills.append(skill)

    return found_skills, missing_skills


def generate_roadmap(missing_skills):
    """Create a simple but useful learning roadmap."""

    learning_details = {

        "Python": {
            "Goal": "Build strong Python programming fundamentals",
            "Topics": "Variables, loops, functions, lists, dictionaries, OOP",
            "Practice": "Solve small Python problems and build mini projects"
        },

        "SQL": {
            "Goal": "Learn SQL for data querying and analysis",
            "Topics": "SELECT, WHERE, GROUP BY, ORDER BY, JOIN",
            "Practice": "Practice queries using a sample database"
        },

        "Excel": {
            "Goal": "Learn Excel for data analysis",
            "Topics": "Formulas, Pivot Tables, Charts, VLOOKUP/XLOOKUP",
            "Practice": "Analyze a sample dataset in Excel"
        },

        "Pandas": {
            "Goal": "Learn data manipulation using Pandas",
            "Topics": "DataFrames, filtering, grouping, cleaning, merging",
            "Practice": "Analyze CSV datasets using Pandas"
        },

        "Power BI": {
            "Goal": "Learn data visualization using Power BI",
            "Topics": "Dashboards, charts, filters, DAX basics",
            "Practice": "Create a simple interactive dashboard"
        },

        "Machine Learning": {
            "Goal": "Understand basic machine learning concepts",
            "Topics": "Regression, classification, training, testing, evaluation",
            "Practice": "Build a small ML model using scikit-learn"
        },

        "scikit-learn": {
            "Goal": "Learn machine learning implementation with scikit-learn",
            "Topics": "Model training, preprocessing, metrics, pipelines",
            "Practice": "Train and evaluate a simple classification model"
        },

        "FastAPI": {
            "Goal": "Learn how to build APIs using FastAPI",
            "Topics": "Routes, request handling, response models, API testing",
            "Practice": "Create an API for a simple ML model"
        },

        "Docker": {
            "Goal": "Learn containerization using Docker",
            "Topics": "Images, containers, Dockerfile, ports",
            "Practice": "Containerize a small Python application"
        },

        "Deep Learning": {
            "Goal": "Understand deep learning fundamentals",
            "Topics": "Neural networks, activation functions, training",
            "Practice": "Build a simple neural network model"
        },

        "LLM": {
            "Goal": "Understand Large Language Model fundamentals",
            "Topics": "Prompts, tokens, embeddings, model APIs",
            "Practice": "Build a small LLM-based application"
        },

        "RAG": {
            "Goal": "Learn Retrieval-Augmented Generation basics",
            "Topics": "Embeddings, vector databases, retrieval, prompting",
            "Practice": "Build a simple document question-answering system"
        },

        "APIs": {
            "Goal": "Learn how applications communicate through APIs",
            "Topics": "HTTP methods, JSON, requests, responses, REST",
            "Practice": "Connect a Python application to a public API"
        },

        "NLP": {
            "Goal": "Learn Natural Language Processing fundamentals",
            "Topics": "Tokenization, text cleaning, classification, embeddings",
            "Practice": "Build a basic text classification project"
        },

        "Transformers": {
            "Goal": "Understand transformer-based NLP models",
            "Topics": "Attention, tokenizers, pretrained models",
            "Practice": "Use a pretrained transformer for text classification"
        },

        "Hugging Face": {
            "Goal": "Learn how to use Hugging Face models",
            "Topics": "Transformers library, tokenizers, pipelines",
            "Practice": "Run a pretrained NLP model"
        },

        "OpenCV": {
            "Goal": "Learn basic computer vision using OpenCV",
            "Topics": "Images, resizing, filtering, edge detection",
            "Practice": "Build a simple image-processing project"
        },

        "CNN": {
            "Goal": "Understand Convolutional Neural Networks",
            "Topics": "Convolution, pooling, feature maps",
            "Practice": "Build a basic image classification model"
        },

        "YOLO": {
            "Goal": "Learn object detection using YOLO",
            "Topics": "Object detection, bounding boxes, confidence scores",
            "Practice": "Run YOLO on sample images"
        }
    }

    roadmap = []

    for week, skill in enumerate(missing_skills, start=1):

        details = learning_details.get(
            skill,
            {
                "Goal": f"Learn the fundamentals of {skill}",
                "Topics": f"Core concepts and practical use of {skill}",
                "Practice": f"Complete a small practice task using {skill}"
            }
        )

        roadmap.append({
            "Week": f"Week {week}",
            "Topic": skill,
            "Goal": details["Goal"],
            "Topics": details["Topics"],
            "Practice": details["Practice"]
        })

    return roadmap