# Django Views and Templates Lab

This project demonstrates the use of Django views and templates for rendering dynamic web pages.

## How the App is Built

This Django app is structured to demonstrate best practices for building web applications with views and templates:

1. **Project and App Structure:**
	- The project was created using:
	  ```sh
	  django-admin startproject myproject
	  python manage.py startapp onlinecourse
	  ```
	- `myproject/` contains project settings and URL configuration.
	- `onlinecourse/` contains models, views, templates, and app logic.

2. **Views:**
	- Both function-based and class-based views are implemented in `onlinecourse/views.py`.
	- Views process requests, interact with models, and pass data to templates.

	- HTML templates are stored in the `templates/` directory (often within the app or at the project level).
	- Templates use Django’s template language to render dynamic content.

4. **Static Files:**
	- CSS, JavaScript, and images are placed in the `static/` directory.
	- Static files are served in development and can be collected for production.

5. **URL Routing:**
	- URLs are mapped to views in `myproject/urls.py` and `onlinecourse/urls.py`.

This structure makes it easy to extend the app with new features, maintain clean separation of concerns, and follow Django’s recommended patterns for scalable web development.

## Transition from Project 05 to 06

In **Project 05**, you learned how to use and customize the Django admin site for managing your application's data through a powerful web interface. The focus was on backend data management, model registration, and admin customizations.

**Project 06** builds on that foundation by introducing Django views and templates. Here, you move beyond the admin and start building the user-facing part of your application. You will:
- Create function-based and class-based views
- Render dynamic HTML pages using Django templates
- Pass data from views to templates for display
- Organize static files and template directories

### What You Will Learn
- How to map URLs to views and return custom responses
- How to use Django's template language to create dynamic web pages
- How to structure your app for maintainable, scalable web development
- The basics of serving static files and using template inheritance

This lab is essential for anyone looking to build real-world Django web applications with custom user interfaces.

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
- See templates for HTML examples.



### About Django Templates

Django templates are HTML files that can display dynamic data passed from your views. They are stored in the `templates/` directory, often organized by app (e.g., `onlinecourse/templates/onlinecourse/`).

- Templates use double curly braces `{{ variable }}` to display variables from the context.
- Logic such as loops and conditionals use `{% ... %}` tags.
- Templates can extend base templates and use blocks for reusable layouts.

**Example:**
```html
<!-- onlinecourse/templates/onlinecourse/course_list.html -->
<h1>Course List</h1>
<ul>
	{% for course in course_list %}
		<li>{{ course.name }} - {{ course.total_enrollment }}</li>
	{% endfor %}
</ul>
```

Templates are rendered in views using the `render()` function, which combines the template with context data:
```python
return render(request, 'onlinecourse/course_list.html', {'course_list': course_list})
```

This approach separates your HTML from your Python code, making your app easier to maintain and extend.

### Template Inheritance

Django templates support inheritance, allowing you to define a base template with common structure (like headers, footers, and navigation) and extend it in other templates. This keeps your code DRY and makes updates easier.

**Example base.html:**
```html
<!DOCTYPE html>
<html>
<head>
	<title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
	<header>
		<h1>My Site</h1>
	</header>
	<nav>
		<!-- Navigation links -->
	</nav>
	<main>
		{% block content %}{% endblock %}
	</main>
	<footer>
		&copy; 2026
	</footer>
</body>
</html>
```

**Example child template:**
```html
{% extends "base.html" %}

{% block title %}Course List{% endblock %}

{% block content %}
<h2>Course List</h2>
<ul>
  {% for course in course_list %}
	<li>{{ course.name }}</li>
  {% endfor %}
</ul>
{% endblock %}
```

This way, all your pages share a consistent layout, and you only need to define unique content in each child template.
