# AI Resume Screening & Candidate Ranking System (ATS with AI)

An AI-powered Applicant Tracking System that analyzes resumes, extracts skills using NLP, compares candidates with job descriptions using Sentence-BERT embeddings, ranks applicants, and provides intelligent resume improvement suggestions.

---

## 🚀 Key Highlights

- AI-powered semantic resume-job matching (Sentence-BERT)
- Intelligent candidate ranking system
- Skill extraction and skill-gap analysis
- AI-based resume improvement suggestions
- Multi-resume screening system (ATS workflow)
- Flask-based full-stack web application

---

## 🧠 AI & ML Features

### 🔹 Semantic Matching (BERT-Based)
- Uses Sentence-BERT (`all-MiniLM-L6-v2`)
- Understands meaning, not just keywords
- More accurate than TF-IDF

---

### 🔹 Hybrid Scoring System
Final score is calculated using:

- 40% Semantic similarity (BERT)
- 60% Skill matching

---

### 🔹 Skill Intelligence
- Extracts skills from resume
- Compares with job description
- Identifies missing skills

---

### 🔹 AI Resume Feedback Engine
Provides:

- Skill gap analysis
- Resume improvement suggestions
- Career optimization tips

---

## 👥 Candidate Ranking System

- Upload multiple resumes
- Compare against job description
- Automatically rank candidates
- Display top matches first

---

## 💾 Database Storage (SQLite)

Stores:

- Candidate name
- Extracted skills
- Match score
- Missing skills

---

## 🛠️ Tech Stack

- Python
- Flask
- Sentence-Transformers (BERT)
- Scikit-learn
- NLP (Text Processing)
- PyPDF2
- SQLite
- HTML, CSS

---

## 📂 Project Structure

```
AI Resume Screening System

├── app.py
├── models/
│   └── matcher.py
├── utils/
│   ├── pdf_reader.py
│   ├── text_cleaner.py
│   ├── skill_extractor.py
│   └── feedback_generator.py
├── database/
│   └── db.py
├── templates/
│   ├── index.html
│   ├── result.html
│   └── dashboard.html
├── uploads/
├── requirements.txt
└── README.md
```

---

## 🔄 Workflow

```
Resume Upload
     ↓
PDF Text Extraction
     ↓
NLP Preprocessing
     ↓
Skill Extraction
     ↓
Job Description Processing
     ↓
Sentence-BERT Embeddings
     ↓
Semantic Similarity Score
     ↓
Skill Matching Score
     ↓
Final ATS Score
     ↓
AI Feedback + Ranking
```

---

## 📊 Output Example

### Single Resume Analysis

- Match Score: 87%
- Skills: Python, ML, SQL
- Missing Skills: Docker, AWS
- AI Feedback: Improvement suggestions

---

### Multi Resume Ranking

| Candidate | Score |
|----------|------|
| Resume1.pdf | 92% |
| Resume2.pdf | 85% |
| Resume3.pdf | 73% |

---

## 🔮 Future Improvements

- Add React frontend dashboard
- Deploy on cloud (AWS / Render / Azure)
- Add authentication system (Recruiter login)
- Generate downloadable PDF reports
- Add resume chatbot assistant (LLM-based)
- Add analytics dashboard (charts & insights)

---

## 👨‍💻 Author

**Kothalanka Siva Ganesh**

AI/ML Developer | NLP Enthusiast | Python Engineer

---

## ⭐ Why this project stands out

✔ Uses modern NLP (Sentence-BERT)  
✔ Real ATS-like architecture  
✔ End-to-end ML pipeline  
✔ Practical industry use case  
✔ Strong portfolio project for AI/ML roles  