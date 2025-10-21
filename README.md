## Flask Lab Project — CI/CD with Docker & GitHub Actions

A minimal Flask application with automated testing, containerization, and continuous integration using GitHub Actions.

## Team Members & Roles
## Member	Role	Responsibilities

Fatima - Backend & Testing 
Lead Implemented Flask routes (/, /health, /data), handled backend logic, wrote test cases using pytest, configured conftest.py for CI import paths, ensured local and CI tests pass.

Neha - DevOps & Frontend Lead	
Styled and structured frontend (index.html, style.css), created and optimized Dockerfile, set up GitHub Actions CI/CD pipeline, configured workflow triggers, and optionally prepared Docker Hub integration.

## Project Structure

flask_lab_project/
├─ main/
│  ├─ app.py
│  ├─ requirements.txt
│  ├─ Dockerfile
│  ├─ templates/
│  │  └─ index.html
│  ├─ static/
│  │  └─ style.css
│  └─ tests/
│     ├─ test_app.py
│     └─ conftest.py
└─ .github/
   └─ workflows/
      └─ ci-cd.yml

Prerequisites

Python 3.12+

Git

Docker Desktop (for container build/run)

GitHub account with Actions enabled

## How to Build, Test, and Run

1. Run Locally

Windows (PowerShell):

cd .\main
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py


Mac/Linux:

cd main
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py


Visit http://localhost:5000

2. Run Tests
cd main
python -m pytest -q

## Tests cover:

/ homepage

/health status

/data JSON/form echo endpoint

3. Build & Run with Docker
# build image
cd main
docker build -t flask-lab-project:latest .

# run container
docker run -p 5000:5000 flask-lab-project:latest


Then visit http://localhost:5000

To stop:

docker ps
docker stop <container_id>

## CI/CD Pipeline — GitHub Actions

File: .github/workflows/ci-cd.yml

✅ What happens on each git push or pull request:

Check out code from repo

Set up Python environment

Install dependencies and run pytest

Build Docker image

(Optional) Push to Docker Hub if secrets are set

📝 To enable Docker Hub push:

Create Docker Hub access token

Add GitHub Secrets:

DOCKERHUB_USERNAME

DOCKERHUB_TOKEN

Push to main → image pushed to:

docker.io/<username>/flask-lab-project:latest

🧾 Submission Checklist

✅ Flask app working (/, /health, /data)

✅ Tests written and passing

✅ Dockerfile working and image runs

✅ GitHub Actions pipeline green (build + test + Docker)

✅ README.md with team roles & run instructions

📸 Screenshots attached in repo or slides:

Actions success ✅

Docker run terminal 🐳

Browser at http://localhost:5000 🌐

🛠️ Troubleshooting
Issue	Fix
pytest can’t find app	Make sure conftest.py exists in tests
Powershell venv activation blocked	Run Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
Workflow not running	Ensure file is in .github/workflows/ and do a git commit --allow-empty -m "Trigger CI"
Docker Hub push skipped	Make sure secrets are set & branch is main
🏁 Credits

Fatima — Backend & Testing

Neha — DevOps & Frontend

📅 CI/CD fully automated with GitHub Actions
🐳 Containerization using Docker
🧪 Tested with pytest
