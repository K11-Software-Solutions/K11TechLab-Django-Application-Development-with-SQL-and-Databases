
# Class-Based and Generic Views Lab

This project demonstrates the use of class-based and generic views in Django for building scalable web applications.

## Difference Between Project 06 and 07

**Project 06: Django Views and Templates**
- Focuses on introducing Django views and templates.
- Uses both function-based views (FBVs) and some basic class-based views (CBVs).
- Demonstrates how to map URLs to views, pass data to templates, and render dynamic HTML using Django’s template language.
- Emphasizes the basics of serving static files, organizing templates, and using template inheritance.
- Example views are written as functions, showing the fundamentals of request handling and response rendering.

**Project 07: Class-Based and Generic Views**
- Focuses on Django’s class-based views (CBVs) and generic views for more scalable and maintainable code.
- Replaces most function-based views with class-based views, such as `ListView`, `DetailView`, and custom CBVs.
- Demonstrates how to use Django’s built-in generic views to reduce boilerplate and follow DRY principles.
- Shows how to override methods like `get_queryset()` and use attributes to customize view behavior.
- Encourages a more object-oriented approach, making it easier to extend and reuse view logic.

**Summary:**
Project 06 teaches the basics of Django views and templates, while Project 07 builds on that foundation by introducing class-based and generic views for cleaner, more scalable Django applications.

## Structure
- `manage.py`: Django management script
- `requirements.txt`: Python dependencies
- `myproject/`: Project settings
- `onlinecourse/`: Main app
- `static/`: Static files

## Setup
1. Create a virtual environment: `python -m venv djangoenv`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Start server: `python manage.py runserver`


## Main Views in This Project

The key views implemented in `onlinecourse/views.py` are:

- **CourseListView**: A class-based view inheriting from Django’s `ListView`. It displays a list of courses, ordered by total enrollment, and renders the course list template.
- **CourseDetailsView**: A class-based view inheriting from `DetailView`. It shows details for a single course using the course detail template.
- **EnrollView**: A custom class-based view inheriting from `View`. It handles POST requests to enroll a user in a course, increments the enrollment count, and redirects to the course details page.

These views demonstrate Django’s object-oriented approach to handling requests, making code more reusable and maintainable compared to function-based views.

## Notes
- Uses SQLite3 by default.
- See views for usage examples.