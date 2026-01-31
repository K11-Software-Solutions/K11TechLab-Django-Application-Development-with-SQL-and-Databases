# Online Course Django Admin Lab

This project demonstrates Django admin site customization for an online course application.

## Difference Between Project 04 and 05

**Project 04** focuses on setting up a basic Django project with Docker support and a simple app structure. It demonstrates how to containerize a Django application and run it locally or in the cloud, but does not include advanced admin customizations.

**Project 05** builds on the basics by showcasing Django's powerful admin interface. It demonstrates how to:
- Register models with the admin site
- Customize admin forms, list displays, filters, and search
- Manage related objects directly from the admin
- Use the admin for efficient data entry and management

This project is ideal for learning how to leverage Django's admin for real-world applications, such as managing courses, instructors, learners, and enrollments.

## How the Admin Site is Built

1. **Model Registration:**
	- All relevant models (Course, Instructor, Learner, etc.) are registered in `adminsite/admin.py` using `admin.site.register()` or custom admin classes.

2. **Customization:**
	- The admin interface is customized using Django's `ModelAdmin` classes. This includes:
	  - Customizing list display columns (`list_display`)
	  - Adding filters (`list_filter`)
	  - Enabling search (`search_fields`)
	  - Inline editing of related models (using `TabularInline` or `StackedInline`)
	  - Custom form layouts and validation

3. **Media and Images:**
	- The admin supports image uploads (e.g., for course images) using Django's `ImageField` and the Pillow library.

4. **Usage:**
	- After running migrations and creating a superuser (`python manage.py createsuperuser`), you can log in to the admin site at `/admin/` and manage all aspects of the online course application through a user-friendly web interface.



## Structure
- `manage.py`: Django management script
- `requirements.txt`: Python dependencies
- `adminsite/`: Main Django app (contains models, admin customizations, and app logic)
- `myproject/`: Project settings

## Setup
1. Create a virtual environment: `python -m venv djangoenv`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Start server: `python manage.py runserver`

## Notes
- Uses SQLite3 by default.
- See `admin.py` for admin customizations.

## How to Set Up URLs, Create Views, and Customize the Admin

### Setting Up URLs
1. Open `myproject/urls.py`.
2. To enable the admin site, ensure you have:
	```python
	from django.contrib import admin
	from django.urls import path

	urlpatterns = [
		 path('admin/', admin.site.urls),
	]
	```
3. To add your own app views, import `include` and add your app's URLs:
	```python
	from django.urls import path, include
	urlpatterns = [
		 path('admin/', admin.site.urls),
		 path('', include('adminsite.urls')),
	]
	```
	Then create an `urls.py` file in your app directory (`adminsite/urls.py`).

### Creating Views
1. In `adminsite/views.py`, define your view functions or classes:
	```python
	from django.http import HttpResponse

	def home(request):
		 return HttpResponse('Hello, world!')
	```
2. In `adminsite/urls.py`, map URLs to your views:
	```python
	from django.urls import path
	from . import views

	urlpatterns = [
		 path('', views.home, name='home'),
	]
	```

### Customizing the Admin
1. Open `adminsite/admin.py`.
2. Register your models:
	```python
	from django.contrib import admin
	from .models import Course
	admin.site.register(Course)
	```
3. For advanced customization, create a custom admin class:
	```python
	class CourseAdmin(admin.ModelAdmin):
		 list_display = ('name', 'description')
		 search_fields = ('name',)
	admin.site.register(Course, CourseAdmin)
	```
4. You can add filters, inlines, and custom forms for a richer admin experience.


## How to Log In to the Admin Site

1. Make sure your server is running:
	```sh
	python manage.py runserver
	```
2. Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
3. Log in using your superuser credentials.
	- If you haven't created a superuser yet, run:
	  ```sh
	  python manage.py createsuperuser
	  ```
	- Follow the prompts to set a username, email, and password.
	- Use these credentials to log in to the admin site.


See Django documentation for more details: https://docs.djangoproject.com/en/stable/ref/contrib/admin/

