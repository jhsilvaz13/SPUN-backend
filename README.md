# SPUN - Simulacro Prueba de la Universidad Nacional

Project for the group Turing Box, the aim is to aid student to pass the university exam.

## Clone repository and start project

You need to have a GitHub account (probably you already do) and the SSH set up and running in
your computer with GitHub credentials. For reference I made an article on [how to set up SSH with GitHub](https://kinsta.com/blog/generate-ssh-key/).

## Backend Requirements

* Python - Pip - FastAPI
* Uvicorn

```bash
git clone git@github.com:SPUN-UNAL/SPUN-backend.git
cd SPUN-backend
python -m .venv
python -m venv .venv
source .venv/bin/activate
uvicorn main:app --reload
```

## Backend local development

* Now you can open your browser and interact with these URLs:

- http://127.0.0.1:8000