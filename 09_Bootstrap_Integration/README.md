# Bootstrap Integration Lab

## What is Bootstrap Integration?
Bootstrap integration in this project means incorporating the Bootstrap CSS framework into Django templates to create modern, responsive, and visually appealing web pages. Bootstrap provides ready-to-use styles and components (like navigation bars, forms, buttons, and grids) that help ensure the site looks good on all devices without writing custom CSS from scratch. In this lab, Bootstrap is included via CDN links in the HTML templates, and its classes are used to style forms, navigation, and layout elements throughout the app.

This project demonstrates how to integrate Bootstrap with Django for responsive web design.

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
- Uses SQLite3 by default.
- Bootstrap is included via CDN and used in these template files:
	- `onlinecourse/templates/onlinecourse/course_list.html`
	- `onlinecourse/templates/onlinecourse/course_detail.html`
	- `onlinecourse/templates/onlinecourse/user_login.html`
	- `onlinecourse/templates/onlinecourse/user_registration.html`
	These files use Bootstrap classes for layout, navigation, and forms. No custom Bootstrap integration is present in static CSS files; all styling is handled through Bootstrap classes in the templates.


# Advantages of Using Bootstrap
Bootstrap offers several benefits for web development in Django projects:
- **Responsive Design:** Automatically adapts layouts for mobile, tablet, and desktop screens.
- **Pre-built Components:** Provides ready-to-use navigation bars, forms, buttons, alerts, and more.
- **Consistent Styling:** Ensures a uniform look and feel across all pages and browsers.
- **Faster Development:** Reduces the need to write custom CSS, speeding up UI creation.
- **Customizable:** Easily override or extend styles to match project branding.
- **Large Community & Documentation:** Extensive resources and support for troubleshooting and learning.