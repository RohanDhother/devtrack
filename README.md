# DevTrack

A job application tracker API built with FastAPI, SQLAlchemy, and Alembic.

Built as a portfolio project alongside a structured backend engineering course,
practising modern Python async patterns.

## Tech Stack

- **FastAPI** — async Python web framework
- **SQLAlchemy** — async ORM with mapped column syntax
- **Alembic** — database migrations
- **SQLite** — lightweight local database (aiosqlite async driver)
- **uv** — fast Python package manager

## Features

- Create, read, update and delete job applications
- Track company, role, status, date applied, and notes
- Auto-generated timestamps on creation
- Full async database layer
- Interactive API docs at `/docs`

## Getting Started

```bash
git clone https://github.com/RohanDhother/devtrack.git
cd devtrack
uv venv && source .venv/bin/activate
uv sync
alembic upgrade head
uvicorn app.main:app --reload
```

Then open http://localhost:8000/docs

## Status

In active development — features added as new concepts are learned.