# Testing and Evaluation Report

## AI Resume Analyzer & Job Recommendation System

## 1. Purpose of Testing

The purpose of testing is to verify that the AI Resume Analyzer performs its main functions correctly and consistently.

The testing focuses on:

- Resume text extraction
- Skill detection
- Job-role recommendation
- Skill-gap analysis
- Readiness-score calculation
- Learning-roadmap generation
- Overall application usability

---

## 2. Functional Testing

| Test | Expected Result | Status |
|---|---|---|
| PDF Resume Upload | PDF resume should upload successfully | PASS |
| DOCX Support | Application accepts DOCX files | PASS |
| Resume Text Extraction | Text should be extracted from the uploaded resume | PASS |
| Text Cleaning | Resume text should be normalized for analysis | PASS |
| Skill Detection | Technical skills should be detected from resume text | PASS |
| Job Recommendation | Top matching job roles should be displayed | PASS |
| Skill Gap Analysis | Found and missing skills should be displayed | PASS |
| Readiness Score | Percentage of required skills found should be calculated | PASS |
| Learning Roadmap | Roadmap should be generated for missing skills | PASS |
| Streamlit Interface | Results should be displayed without application errors | PASS |

---

## 3. Job Recommendation Test Cases

Five controlled test cases were created, with one test case representing each supported job role.

| Test Case | Resume Skills | Expected Top Role | Result |
|---|---|---|---|
| 1 | Python, Pandas, Excel, Power BI, SQL | Data Analyst | PASS |
| 2 | Python, Machine Learning, scikit-learn, Docker, FastAPI | Machine Learning Engineer | PASS |
| 3 | Python, Machine Learning, Deep Learning, LLM, RAG, APIs | AI Engineer | PASS |
| 4 | Python, NLP, Transformers, Hugging Face, Machine Learning | NLP Engineer | PASS |
| 5 | Python, OpenCV, CNN, YOLO, Deep Learning | Computer Vision Engineer | PASS |

---

## 4. Automated Test Result

The automated job-matching test was executed using:

```bash
python tests/test_job_matching.py
```

The final result was:

```text
Passed: 5/5
Accuracy: 100%
```

All five predefined job-role matching test cases passed.

The 100% value represents accuracy only on this small controlled test set. It should not be interpreted as 100% accuracy on real-world resumes.

---

## 5. Job Matching Evaluation

The system uses a hybrid job-matching method consisting of:

```text
70% Skill Overlap
+
30% TF-IDF Cosine Similarity
```

Skill overlap gives more importance to whether the resume contains the skills required by a job role.

TF-IDF and cosine similarity provide an additional text-similarity measure.

The final scores are sorted from highest to lowest to generate the top job recommendations.

---

## 6. Sample Application Result

During testing, a sample technical resume produced 15 detected skills, including:

```text
Python
C++
Pandas
NumPy
Matplotlib
Power BI
Excel
Machine Learning
Deep Learning
NLP
LLM
Docker
Git
GitHub
APIs
```

One observed recommendation result was:

```text
1. AI Engineer — 61.37% Match
2. Data Analyst — 60.10% Match
3. Machine Learning Engineer — 49.09% Match
```

The exact recommendations and percentages depend on the contents of the uploaded resume.

---

## 7. Skill Gap and Readiness Testing

The target-role feature was tested by selecting a job role and comparing its required skills against the skills detected in the resume.

The system successfully displays:

- Skills Found
- Missing Skills
- Number of required skills detected
- Readiness percentage

The readiness score is calculated as:

```text
Readiness =
Number of Required Skills Found
-------------------------------- × 100
Total Number of Required Skills
```

---

## 8. Learning Roadmap Testing

For each missing skill, the system generates:

- Week number
- Skill/topic
- Learning goal
- Important topics
- Practice activity

For example:

```text
Week 1 — SQL

Goal:
Learn SQL for data querying and analysis

Topics:
SELECT, WHERE, GROUP BY, ORDER BY, JOIN

Practice:
Practice queries using a sample database
```

This feature was successfully displayed in the Streamlit application.

---

## 9. Resume Section Detection

The system also uses heading-based detection for common resume sections:

- Education
- Experience
- Projects

The feature works when recognizable section headings are present in the extracted resume text.

If a heading is missing or formatted differently, the corresponding section may not be detected.

---

## 10. Limitations

The current project has several limitations:

1. The job-role database contains a limited number of roles.
2. Skill detection depends on the predefined skill dictionary.
3. Resume section extraction depends on recognizable headings.
4. TF-IDF does not understand semantic meaning as deeply as modern embedding models.
5. The automated evaluation currently contains only five controlled job-matching test cases.
6. Real resumes can have different formats, wording, and layouts.
7. Match percentages should be interpreted as recommendation scores rather than guarantees of employability.

---

## 11. Overall Evaluation

The current version successfully performs the main workflow:

```text
Resume Upload
→ Text Extraction
→ Text Cleaning
→ Resume Section Detection
→ Skill Detection
→ Job Matching
→ Top Role Recommendations
→ Skill Gap Analysis
→ Readiness Score
→ Learning Roadmap
```

The five controlled job-matching test cases achieved:

```text
5/5 PASS
```

The system therefore meets the main functional objectives of the current project prototype while leaving scope for larger datasets and more advanced NLP methods in future versions.