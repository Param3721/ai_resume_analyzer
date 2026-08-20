# 📄 AI Resume Analyzer & Job Recommendation System

An intelligent resume analysis application built using **Python, Streamlit, NLP, TF-IDF, and Machine Learning techniques**.

The system analyzes a user's resume, detects technical skills, recommends suitable job roles, identifies missing skills, calculates job readiness, and generates a personalized learning roadmap.

---

## 🚀 Live Demo

The application is deployed using **Streamlit Community Cloud**.

### 🔗 Live Application

https://param-ai-resume-analyzer.streamlit.app

---

## 🎯 Project Objective

The main objective of this project is to help students and job seekers understand how well their current skills match different technical job roles.

The application automatically analyzes an uploaded resume and provides:

- Resume text extraction
- Resume section detection
- Technical skill detection
- Job role recommendations
- Job match scores
- Skill gap analysis
- Target role readiness score
- Personalized learning roadmap

---

## ✨ Project Features

### 📄 1. Resume Text Extraction

The user can upload a resume in:

- PDF
- DOCX

The application automatically extracts the text from the uploaded resume.

---

### 📑 2. Resume Section Detection

The system detects important sections of the resume such as:

- Education
- Experience
- Projects

This helps organize and understand the resume content.

---

### 🧠 3. Skill Detection

The system identifies technical skills present in the resume using a predefined skill dictionary.

Some examples include:

- Python
- C++
- Java
- SQL
- Pandas
- NumPy
- Matplotlib
- Power BI
- Excel
- Machine Learning
- Deep Learning
- NLP
- LLM
- OpenCV
- Docker
- Git
- GitHub
- APIs

---

## 💼 4. Job Role Recommendation

The application compares the resume with predefined technical job roles and recommends the **Top 3 most suitable roles**.

The current system supports roles such as:

- AI Engineer
- Data Analyst
- Machine Learning Engineer
- NLP Engineer
- Computer Vision Engineer

The recommendations are displayed with match percentages and progress bars.

---

## 📊 5. Hybrid Job Matching Algorithm

The job recommendation system uses a hybrid matching approach.

The final job match score combines:

```text
70% Skill Overlap
+
30% TF-IDF Cosine Similarity
```

### Skill Overlap

The system checks how many required skills for a particular job role are present in the resume.

### TF-IDF

TF-IDF converts resume text and job-role requirements into numerical vectors.

### Cosine Similarity

Cosine similarity measures how similar the resume vector is to each job-role vector.

The final scores are sorted from highest to lowest to generate the job recommendations.

---

## 🎯 6. Target Role Skill Gap Analysis

The user can select a target job role.

The system then compares the skills detected in the resume with the skills required for that role.

It displays:

### ✅ Skills Found

Skills already present in the resume.

### ❌ Missing Skills

Important skills that should be learned for the selected role.

---

## 📈 7. Target Role Readiness Score

The application calculates how prepared the user currently is for the selected target role.

The readiness score is calculated using:

```text
Readiness Score =
(Number of Required Skills Found / Total Required Skills) × 100
```

The result is displayed as a percentage and progress bar.

The readiness percentage is a project-based skill coverage score and should not be considered a guarantee of employment.

---

## 🗺️ 8. Personalized Learning Roadmap

Based on the missing skills, the application generates a week-wise learning roadmap.

Each roadmap step can contain:

- Week number
- Skill to learn
- Learning goal
- Important topics
- Practice activity

Example:

```text
Week 1 — SQL

Goal:
Learn SQL for data querying and analysis

Topics:
SELECT, WHERE, GROUP BY, ORDER BY, JOIN

Practice:
Practice SQL queries using a sample database
```

---

# 🔄 System Workflow

The complete application follows this workflow:

```text
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Resume Section Detection
      ↓
Skill Detection
      ↓
Hybrid Job Matching
      ↓
Top 3 Job Recommendations
      ↓
Target Role Selection
      ↓
Skill Gap Analysis
      ↓
Readiness Score
      ↓
Personalized Learning Roadmap
      ↓
Streamlit Results
```

---

# 🏗️ Project Structure

```text
ai_resume_analyzer/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── section_extractor.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
├── tests/
│   ├── test_cases.csv
│   └── test_job_matching.py
│
├── reports/
│   ├── testing_evaluation.md
│   └── AI_Resume_Analyzer_Project_Report.docx
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| Pandas | CSV and data processing |
| scikit-learn | TF-IDF and cosine similarity |
| PyPDF | PDF resume text extraction |
| python-docx | DOCX resume text extraction |
| NLP | Resume text processing |
| Git | Version control |
| GitHub | Project repository |
| Streamlit Community Cloud | Application deployment |

---

# 🧩 Main Project Modules

## `app.py`

Controls the Streamlit interface and connects all components of the application.

## `resume_parser.py`

Extracts text from PDF and DOCX resumes.

## `text_cleaner.py`

Cleans and normalizes extracted resume text.

## `section_extractor.py`

Detects common resume sections such as Education, Experience, and Projects.

## `skill_extractor.py`

Detects technical skills from the resume using the skill dictionary.

## `job_matcher.py`

Calculates job-role matching scores using skill overlap and TF-IDF cosine similarity.

## `roadmap_generator.py`

Performs skill-gap analysis and generates the personalized learning roadmap.

---

# 🧪 Testing and Evaluation

The job recommendation system was tested using controlled test cases for the five supported job roles.

The automated test produced:

```text
Passed: 5/5
Accuracy: 100%
```

The five test cases included:

| Test | Expected Role | Result |
|---|---|---|
| 1 | Data Analyst | PASS |
| 2 | Machine Learning Engineer | PASS |
| 3 | AI Engineer | PASS |
| 4 | NLP Engineer | PASS |
| 5 | Computer Vision Engineer | PASS |

> **Note:** 100% refers only to the five controlled test cases. It does not mean the system has 100% accuracy on all real-world resumes.

The detailed testing report is available at:

```text
reports/testing_evaluation.md
```

---

# 💻 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/Param3721/ai_resume_analyzer.git
```

Move into the project directory:

```bash
cd ai_resume_analyzer
```

---

## 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

```bash
streamlit run app.py
```

Streamlit will open the application in your browser.

---

# 🧪 Running the Automated Test

Run:

```bash
python tests/test_job_matching.py
```

The current controlled test set should produce:

```text
Passed: 5/5
Accuracy: 100%
```

---

# 📦 Main Dependencies

The project uses:

```text
streamlit
pypdf
python-dotenv
google-generativeai
python-docx
scikit-learn
pandas
```

The exact environment requirements are maintained in:

```text
requirements.txt
```

---

# ⚠️ Current Limitations

The current version has some limitations:

1. The number of supported job roles is limited.
2. Skill detection depends on the predefined skill dictionary.
3. Resume section detection depends on recognizable section headings.
4. TF-IDF has limited understanding of semantic meaning.
5. The automated evaluation currently contains only five controlled test cases.
6. Real-world resumes can have very different formats and writing styles.
7. Match and readiness percentages are recommendation scores, not guarantees of employability.

---

# 🔮 Future Improvements

Future versions of the project can include:

- More job roles
- Larger skill datasets
- Sentence-transformer embeddings
- Semantic resume matching
- Job-description upload and comparison
- Resume improvement suggestions
- More advanced resume section detection
- Larger automated testing datasets
- Improved NLP-based skill extraction

---

# 📄 Project Report

The complete project report is available inside:

```text
reports/AI_Resume_Analyzer_Project_Report.docx
```

The testing and evaluation report is available inside:

```text
reports/testing_evaluation.md
```

---

# 🌐 Deployment

The application is deployed on **Streamlit Community Cloud**.

Live application:

https://param-ai-resume-analyzer.streamlit.app

---

# 👨‍💻 Author

**Param Malhotra**

GitHub: **Param3721**

---

# 📌 Project Status

✅ Resume Upload  
✅ Text Extraction  
✅ Resume Section Detection  
✅ Skill Detection  
✅ Hybrid Job Matching  
✅ Top 3 Job Recommendations  
✅ Skill Gap Analysis  
✅ Readiness Score  
✅ Personalized Learning Roadmap  
✅ Automated Testing  
✅ Project Documentation  
✅ Streamlit Cloud Deployment  

**Project successfully completed and deployed.**