# CI/CD with GitHub Actions

A hands-on practice repo for CI/CD pipelines using GitHub Actions, pytest and Docker.

## The app

A minimal Flask server (`server.py`) with one route that returns "DevOps is awesome!".

## The pipelines

- **CI** (`.github/workflows/ci.yml`): on every pull request to `main`, sets up Python 3.11, installs dependencies, and runs the test suite with pytest (`app_test.py`).
- **CD** (`.github/workflows/cd.yml`): on every push to `main`, logs in to Docker Hub, builds a Docker image from the repo's `Dockerfile`, and pushes it tagged with the commit SHA.

## Run locally

```bash
pip install -r requirements.txt
python server.py
# open http://localhost:5000
```

Run the tests:

```bash
pytest
```
