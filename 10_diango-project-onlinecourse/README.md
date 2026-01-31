# Online Course Final Project

This is the capstone Django project for the course, extending the onlinecourse app with advanced features such as assessments, user authentication, and cloud deployment support.

## Features
- Course listing, detail, and enrollment
- User registration, login, and logout
- Assessment and quiz functionality
- Admin interface for managing courses and users
- Responsive UI with Bootstrap
- SQLite3 database (default)
- Ready for deployment to IBM Cloud Foundry (manifest.yml, Procfile)

## Project Structure
- `manage.py`: Django management script
- `requirements.txt`: Python dependencies
- `myproject/`: Project settings
- `onlinecourse/`: Main app (models, views, templates)
- `static/`: Static files (CSS, images)
- `project_submission/`: Submission and documentation files

## Setup
1. Create a virtual environment: `python -m venv djangoenv`
2. Activate the environment and install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Deployment
- To deploy on IBM Cloud Foundry, use the provided `manifest.yml` and `Procfile`.
- The project can be adapted for other platforms as needed.

## Notes
- See the ER diagram for the data model (link in project_submission/ or README).
- All features are modular and follow Django best practices.
- For more details, see comments in source files and the documentation folder.
