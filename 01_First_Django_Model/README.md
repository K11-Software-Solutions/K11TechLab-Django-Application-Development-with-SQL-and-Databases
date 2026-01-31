# First Django Model Lab

This project demonstrates the creation of a simple Django model using the ORM. It is designed for beginners to understand the basics of Django models and migrations.

## Structure
- `manage.py`: Django management script
- `settings.py`: Django settings
- `requirements.txt`: Python dependencies
- `orm/`: Contains model definitions
- `test.py`: Script to test model operations

## Setup
1. Create a virtual environment: `python -m venv djangoenv`
2. Activate the environment and install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Run tests: `python test.py`

## Notes
- Uses SQLite3 by default.
- For more details, see comments in source files.