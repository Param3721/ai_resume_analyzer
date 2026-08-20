# AI Resume Analyzer & Job Recommendation System

An AI-based resume analysis system built using Python, NLP, Machine Learning, and Streamlit.

The application analyzes a user's resume, detects technical skills, recommends suitable job roles, identifies missing skills for a selected target role, calculates job readiness, and generates a personalized learning roadmap.

---

## Project Overview

Finding the right job role from a resume can be difficult because resumes contain different skills, technologies, and experiences.

This project provides a simple system that automatically analyzes a resume and helps the user understand:

- Skills detected in the resume
- Suitable job roles
- Job-role match percentages
- Skills required for a target role
- Skills currently missing
- Target-role readiness percentage
- Personalized learning roadmap

The application supports resumes in both **PDF** and **DOCX** formats.

---

## Features

### 1. Resume Text Extraction

The user can upload a PDF or DOCX resume.

The application extracts the text from the uploaded resume for further analysis.

### 2. Text Cleaning

The extracted resume text is cleaned and normalized before skill detection and job matching.

### 3. Skill Detection

The system detects technical skills from the resume using a predefined skill dictionary.

Examples include:

- Python
- SQL
- Pandas
- NumPy
- Machine Learning
- Deep Learning
- NLP
- Power BI
- Docker
- Git
- APIs

### 4. Job Role Recommendation

The system recommends the top three job roles based on the contents of the resume.

Currently supported roles include:

- Data Analyst
- Machine Learning Engineer
- AI Engineer
- NLP Engineer
- Computer Vision Engineer

### 5. Hybrid Job Matching

The job-matching system combines two methods:

- **70% Skill Overlap**
- **30% TF-IDF Cosine Similarity**

This allows the application to consider both the required technical skills and the similarity between resume content and job requirements.

### 6. Match Score Visualization

The top three recommended roles are displayed with percentage scores and Streamlit progress bars.

### 7. Skill Gap Analysis

The user can select a target job role.

The application then compares the user's detected skills with the skills required for that role and displays:

- Skills Found
- Missing Skills

### 8. Job Readiness Score

The application calculates the user's readiness for the selected target role.

For example:

```text
Data Analyst Readiness: 80%
4 of 5 required skills found.
```

### 9. Personalized Learning Roadmap

For every missing skill, the application generates a simple learning roadmap containing:

- Learning goal
- Important topics
- Practice activity

Example:

```text
Week 1 — SQL

Goal: Learn SQL for data querying and analysis

Topics: SELECT, WHERE, GROUP BY, ORDER BY, JOIN

Practice: Practice queries using a sample database
```

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- PyPDF
- python-docx
- Git
- GitHub

---

## Project Structure

```text
ai_resume_analyzer/
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
├── tests/
│   ├── test_cases.csv
│   └── test_job_matching.py
│
├── app.py
├── job_matcher.py
├── resume_parser.py
├── roadmap_generator.py
├── skill_extractor.py
├── text_cleaner.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## How the System Works

The application follows this workflow:

```text
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Skill Detection
      ↓
Job Role Matching
      ↓
Top 3 Recommendations
      ↓
Target Role Selection
      ↓
Skill Gap Analysis
      ↓
Readiness Score
      ↓
Learning Roadmap
```

---

## Job Matching Method

The project uses a hybrid matching approach.

### Skill Overlap

For each job role, the system checks how many required skills are present in the resume.

The skill coverage is calculated as:

```text
Matched Skills / Total Required Skills
```

### TF-IDF and Cosine Similarity

TF-IDF converts the resume and job requirements into numerical vectors.

Cosine similarity measures the similarity between the resume vector and each job-role vector.

### Final Match Score

The final score uses:

```text
Final Match Score =
70% Skill Overlap + 30% TF-IDF Similarity
```

The roles are then sorted from highest to lowest match score.

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Param3721/ai_resume_analyzer.git
```

### 2. Open the Project Folder

```bash
cd ai_resume_analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

Streamlit will provide a local address, usually:

```text
http://localhost:8501
```

Open it in a web browser and upload a PDF or DOCX resume.

---

## Testing

A basic job recommendation test suite is included in the `tests` folder.

Run the tests using:

```bash
python tests/test_job_matching.py
```

The test dataset contains five test cases representing the five supported job roles.

Current test result:

```text
Passed: 5/5
Accuracy: 100%
```

This result refers to the project's predefined test cases and should not be interpreted as general real-world model accuracy.

---

## Example Output

For a sample technical resume, the application can display results such as:

```text
Detected Skills:
Python, C++, Pandas, NumPy, Matplotlib, Power BI,
Excel, Machine Learning, Deep Learning, NLP,
LLM, Docker, Git, GitHub, APIs
```

Example job recommendations:

```text
1. AI Engineer — 61.37% Match
2. Data Analyst — 60.10% Match
3. Machine Learning Engineer — 49.09% Match
```

The exact results depend on the uploaded resume and the job-role data.

---

## Future Improvements

The project can be extended in the future by adding:

- More job roles
- Larger skill dictionaries
- More advanced NLP techniques
- Semantic similarity using embeddings
- Resume quality feedback
- Job description upload and comparison
- More extensive automated testing
- Cloud deployment

---

## Conclusion

The AI Resume Analyzer & Job Recommendation System demonstrates how NLP and Machine Learning techniques can be used to analyze resumes and provide career-related recommendations.

The project combines resume parsing, skill extraction, TF-IDF, cosine similarity, skill-gap analysis, and a learning roadmap in an interactive Streamlit application.

---

## Author

**Param Malhotra**

AI Resume Analyzer & Job Recommendation System