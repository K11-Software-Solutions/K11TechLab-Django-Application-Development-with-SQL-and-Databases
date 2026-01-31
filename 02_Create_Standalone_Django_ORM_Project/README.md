# Standalone Django ORM Project

This project demonstrates how to use Django ORM outside of a full Django project. It is useful for scripts and standalone applications that need database access.

## Structure
- `manage.py`: Django management script
- `settings.py`: Django settings
- `standalone/`: Contains standalone ORM usage
- `test.py`: Script to test ORM operations

## Setup
1. Create a virtual environment: `python -m venv djangoenv`
2. Activate and install dependencies: `pip install django`
3. Run: `python test.py`

## Notes
- Uses SQLite3 by default.
- No web server or templates included.

## What is a Standalone Model?
A standalone model in Django refers to using Django's ORM (Object-Relational Mapping) features outside of a traditional Django web application. Instead of requiring the full Django project structure (with apps, views, and templates), you can define models and interact with the database using only the essential Django settings and ORM components. This approach is ideal for scripts, automation, or data processing tasks where you need database access but do not need a web interface.

In this project, the `standalone/models.py` file contains a simple model definition, and you can run database operations directly from scripts like `test.py` or with pytest-based tests. This setup demonstrates how to leverage Django's powerful ORM capabilities in a minimal, script-friendly environment.