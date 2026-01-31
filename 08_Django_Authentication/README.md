# Django Authentication Lab

This project demonstrates user authentication and authorization in Django, including login, logout, and registration features.

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

## Notes

## Authentication Implementation

## Difference Between Project 07 and 08

**Project 07: Class-Based and Generic Views**
- Focuses on scalable, maintainable code using Django’s class-based and generic views (CBVs).
- No authentication or user management features.
- URL patterns do not include login, logout, or registration.
- All users can access all views; no login required.
- Emphasizes DRY principles and object-oriented view logic.

**Project 08: Django Authentication**
- Builds on the CBV foundation by adding full authentication (login, logout, registration).
- Implements login/logout with Django’s built-in views and custom registration with validation.
- URL patterns include `/accounts/login/`, `/accounts/logout/`, and `/accounts/register/` at the project root.
- Some views are protected with `@login_required` or class-based equivalents.
- Templates for login and registration display form errors and navigation links.
- Playwright UI/browser tests are included for authentication flows.
- After login or registration, users are redirected to the course list page.
- Uses Django’s default `User` model for authentication.

**Summary:**
Project 07 focuses on scalable view logic with CBVs, while project 08 adds authentication, user validation, protected views, and UI/browser test automation for authentication flows.

This project implements authentication using Django's built-in authentication system, with custom registration logic:

- **Login/Logout:**
	- Uses Django's built-in `LoginView` and `LogoutView`.
	- URLs `/accounts/login/` and `/accounts/logout/` are configured in the main URLconf (`myproject/urls.py`).
	- The login page uses a custom template: `onlinecourse/templates/onlinecourse/user_login.html`.

- **Registration:**
	- A custom registration view (`register`) and form (`RegistrationForm`) are implemented in `onlinecourse/views.py`.
	- Registration is available at `/accounts/register/` (configured in `myproject/urls.py`).
	- The registration form checks for duplicate usernames and matching passwords.
	- Registration uses the template: `onlinecourse/templates/onlinecourse/user_registration.html`.

- **Permissions:**
	- Views that require authentication use the `@login_required` decorator or Django's class-based view mixins.

- **Templates:**
	- Login and registration templates display form errors and provide navigation links.
	- After login or registration, users are redirected to the course list page.

- **Testing:**
	- Playwright tests are provided for both login and registration UI flows.

- **User Model:**
	- Uses Django's default `User` model for authentication.

See `onlinecourse/views.py` and `myproject/urls.py` for implementation details.