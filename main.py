
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ResumeRequest(BaseModel):
    resume: str
    job_description: str


@app.get("/")
def home():
    return {"message": "AI Resume Analyzer is running!"}


@app.post("/analyze")
def analyze_resume(data: ResumeRequest):
    resume = data.resume
    jd = data.job_description

    return {
        "message": "Resume received successfully!",
        "resume_length": len(resume),
        "jd_length": len(jd)
    }