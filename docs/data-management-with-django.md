# Data Management Using Django

Django provides a powerful and flexible system for managing data in web applications. Its Object-Relational Mapping (ORM) layer allows developers to interact with databases using Python code instead of raw SQL.

## Key Concepts

### 1. Models
- Models are Python classes that define the structure of your database tables.
- Each model maps to a single table in the database.
- Example:
  ```python
  from django.db import models
  class Book(models.Model):
      title = models.CharField(max_length=100)
      author = models.CharField(max_length=50)
      published_date = models.DateField()
  ```

### 2. Migrations
- Migrations are Django’s way of propagating changes you make to your models into the database schema.
- Commands:
  - `python manage.py makemigrations`
  - `python manage.py migrate`

### 3. Querying Data
- Use Django ORM methods to create, read, update, and delete records.
- Examples:
  ```python
  # Create
  book = Book.objects.create(title="Django Basics", author="Alice", published_date="2024-01-01")
  # Read
  books = Book.objects.all()
  # Update
  book.title = "Advanced Django"
  book.save()
  # Delete
  book.delete()
  ```

### 4. Admin Interface
- Django auto-generates an admin interface for managing data.
- Register your models in `admin.py` to use this feature.

### 5. Database Support
- Django supports multiple databases: PostgreSQL, MySQL, SQLite, Oracle, and more.
- Configure your database in `settings.py`.

## Best Practices
- Use model methods and managers for reusable queries.
- Validate data using Django’s built-in validators and model field options.
- Use migrations to keep your database schema in sync with your models.

## Resources
- [Django Models Documentation](https://docs.djangoproject.com/en/stable/topics/db/models/)
- [Django ORM Queries](https://docs.djangoproject.com/en/stable/topics/db/queries/)

---
Django’s ORM and admin interface make data management efficient and developer-friendly.
