# Copilot Instructions for AI Agents

## Project Overview
This workspace contains multiple Django-based projects and labs, each in its own subdirectory. The projects are designed for hands-on learning of Django, SQL, and database integration, with a focus on modularity and progressive complexity.

- Each numbered folder (e.g., `01_First_Django_Model`, `03_CRUD_On_Django_Model_Object`, etc.) is a self-contained Django project or lab.
- The `10_diango-project-onlinecourse` folder contains the final project, which extends the `onlinecourse` app with an assessment feature.
- Most projects use SQLite3 by default, but are compatible with other Django-supported SQL databases.

## Key Patterns and Conventions
- **Project Structure:**
  - Each lab/project has its own `manage.py`, `settings.py`, and `requirements.txt`.
  - Apps are typically found in subfolders like `firstapp/`, `adminsite/`, or `onlinecourse/`.
  - Virtual environments are often named `djangoenv/` and are local to each project.
- **Database:**
  - Default database is SQLite3 (`db.sqlite3`), but can be swapped for PostgreSQL/MySQL as needed.
- **Testing:**
  - Some labs include test scripts (e.g., `test.py`, `read_courses.py`) for validating models and CRUD operations.
- **Deployment:**
  - The final project supports deployment to IBM Cloud Foundry by default, but is adaptable to other platforms.
  - Docker support is present in `04_Django_firstproject_With_Docker` (see `Dockerfile`).

## Developer Workflows
- **Setup:**
  - Create and activate a virtual environment in each project folder (`python -m venv djangoenv`), then install dependencies from `requirements.txt`.
- **Running:**
  - Use `python manage.py runserver` from the relevant project directory.
- **Testing:**
  - Run provided test scripts or use Django's test runner (`python manage.py test`).
- **Database Migrations:**
  - Standard Django migration commands apply: `python manage.py makemigrations`, `python manage.py migrate`.

## Integration Points
- **Cloud Deployment:**
  - For IBM Cloud, use `manifest.yml` and `Procfile` in the final project.
  - Environment variables and cloud-specific configs may be required for other platforms.
- **Docker:**
  - See `04_Django_firstproject_With_Docker/Dockerfile` for containerization patterns.

## Notable Files & Directories
- `10_diango-project-onlinecourse/README.md`: Project-specific instructions and ER diagram link.
- `04_Django_firstproject_With_Docker/Dockerfile`: Example Docker setup for Django.
- `requirements.txt` in each project: Project-specific dependencies.
- `djangoenv/`: Per-project virtual environments (do not share across projects).

## Project-Specific Conventions
- Each lab is independent; do not assume shared state or dependencies between them.
- Hints and instructions may be embedded as comments in source files.
- Naming conventions follow standard Django practices unless otherwise noted.

---
For more details, see the README in each project folder. If a workflow or integration is unclear, check for comments in the relevant `manage.py`, `settings.py`, or test scripts.
