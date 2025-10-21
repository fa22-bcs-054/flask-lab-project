# Flask Lab Project (2-Member Adaptation)

This repository contains a minimal Flask app with CI/CD via GitHub Actions and a Dockerfile.

## Roles (2 Members)

- **Member A — App Lead**: Flask routes, templates, tests (`main/`, `member1_backend/`).
- **Member B — DevOps & Frontend**: CSS/HTML, Dockerfile, GitHub Actions (`main/static`, `main/.github/workflows`, `member2_frontend/`).

> Based on the original lab brief for a 3-person team; adapted here for two members while keeping the same deliverables.

## Run Locally

```bash
cd main
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
# visit http://localhost:5000
```

## Test

```bash
cd main
pytest -q
```

## Docker

```bash
cd main
docker build -t flask-lab-project:latest .
docker run -p 5000:5000 flask-lab-project:latest
```

## CI/CD (GitHub Actions)

- Triggers on pushes/PRs to `main`.
- Steps: install deps → run tests → build Docker image → optionally push to Docker Hub **if** you set repo secrets:
  - `DOCKERHUB_USERNAME`
  - `DOCKERHUB_TOKEN` (a Docker Hub access token)

## Project Structure

```
flask_lab_project/
└── main/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── tests/
    │   └── test_app.py
    ├── templates/
    │   └── index.html
    ├── static/
    │   └── style.css
    └── .github/workflows/
        └── ci-cd.yml
├── member1_backend/
└── member2_frontend/
```

## Submission Checklist

- GitHub repo link
- Screenshot: successful CI/CD run (Actions tab)
- Screenshot: app running via Docker
- **README** updated with member names & exact commands
