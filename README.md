# VacancyBot 🤖

VacancyBot is an intelligent job application assistant that automates the process of searching for vacancies, analyzing resumes, and generating personalized insights for candidates.

## 🚀 Features

- Automated job search
- Resume analysis with AI
- Matching candidate profile with job descriptions
- Personalized feedback
- REST API with FastAPI
- Background task processing
- Database integration with SQLAlchemy

## 🛠 Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite / PostgreSQL
- OpenAI / Gemini API
- Pydantic
- Async programming
- BackgroundTasks

## 📂 Project Structure


```bash
VacancyBot/
│── Config/
│── Controller/
│── Main/
    │── main.py
│── Model/
│── Repository/
│── schema/
│── Service/
```
## 📂 Installation

## ▶️ Running the project

### 1. Activate virtual environment

```bash
source venv/bin/activate
```

### 2. Start server

```bash
fastapi dev Main/main.py
```

### 3. Open documentation

```bash
http://127.0.0.1:8000/docs
```

## 📌 Example Endpoint

POST /resume/vacancy-send-params

```bash
{
  "city": "New York",
  "position": "Backend Developer",
  "salary_min": 3000,
  "salary_max": 7000,
  "country": "USA"
}
```
