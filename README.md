📄 AI Resume & Job Description Analyzer

An AI-powered tool built with Python and FastAPI that compares a resume against a job description, highlights matching and missing skills, and generates personalized suggestions to improve the resume.

✨ Features
Resume parsing: Upload a resume (PDF/DOCX/TXT) and extract clean text
Job description analysis: Paste or upload a job description to extract required skills and keywords
Skill matching: Identifies skills present in both the resume and the job description
Gap detection: Lists important skills and keywords missing from the resume
Match score: Gives an overall compatibility percentage
Personalized suggestions: AI-generated recommendations to improve wording, structure, and keyword coverage
REST API: Clean, documented endpoints with automatic Swagger/OpenAPI docs
🛠️ Tech Stack
Layer	Technology
Language	Python 3.10+
Framework	FastAPI
Server	Uvicorn
NLP / AI	spaCy / scikit-learn / LLM API (configurable)
File parsing	PyPDF2 / pdfplumber, python-docx
Validation	Pydantic

Adjust this table to match the libraries you actually use.

📁 Project Structure
resume-analyzer/
├── app/
│   ├── main.py               # FastAPI app entry point
│   ├── api/
│   │   └── routes.py         # API endpoints
│   ├── services/
│   │   ├── parser.py         # Resume/JD text extraction
│   │   ├── skill_extractor.py# Skill & keyword extraction
│   │   ├── matcher.py        # Matching & scoring logic
│   │   └── suggestions.py    # AI-generated improvement tips
│   ├── models/
│   │   └── schemas.py        # Pydantic request/response models
│   └── utils/
│       └── helpers.py
├── tests/
├── requirements.txt
├── .env.example
└── README.md
🚀 Getting Started
Prerequisites
Python 3.10 or higher
pip
(Optional) An API key for your chosen LLM provider
Installation
bash
# 1. Clone the repository
git clone https://github.com/<your-username>/resume-analyzer.git
cd resume-analyzer

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. (If using spaCy) download the language model
python -m spacy download en_core_web_sm
Configuration

Copy the example environment file and add your keys:

bash
cp .env.example .env
env
LLM_API_KEY=your_api_key_here
LLM_MODEL=your_model_name
MAX_FILE_SIZE_MB=5
Run the Server
bash
uvicorn app.main:app --reload

The API will be available at http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
📡 API Endpoints
Method	Endpoint	Description
GET	/health	Health check
POST	/analyze	Analyze a resume against a job description
POST	/extract-skills	Extract skills from a resume or job description
POST	/suggestions	Generate improvement suggestions only

Update the endpoints to match your implementation.

Example: Analyze a Resume

Request

bash
curl -X POST "http://127.0.0.1:8000/analyze" \
  -F "resume=@resume.pdf" \
  -F "job_description=We are looking for a Python developer with FastAPI, Docker, and AWS experience..."

Response

json
{
  "match_score": 72.5,
  "matching_skills": ["Python", "FastAPI", "REST APIs", "Git"],
  "missing_skills": ["Docker", "AWS", "CI/CD"],
  "suggestions": [
    "Add a project or bullet point that demonstrates Docker usage.",
    "Quantify your achievements, e.g. 'Reduced API latency by 30%'.",
    "Include a dedicated Skills section listing cloud technologies."
  ]
}
🧠 How It Works
Extract: Text is pulled from the uploaded resume and the job description.
Analyze: Skills, keywords, and entities are identified using NLP.
Match: Resume skills are compared against job requirements to compute overlap and a match score.
Suggest: Missing skills and weak areas are passed to an AI model to produce tailored, actionable feedback.
🧪 Running Tests
bash
pytest
🗺️ Roadmap
 Support for more resume formats
 ATS-friendliness check
 Web frontend (React / Streamlit)
 Multi-job comparison
 Docker support and deployment guide
 Export analysis report as PDF
🤝 Contributing

Contributions are welcome!

Fork the repository
Create a feature branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m "Add your feature")
Push to the branch (git push origin feature/your-feature)
Open a Pull Request
📜 License

This project is licensed under the MIT License. See the LICENSE file for details.
