# CRUD on Django Model Objects

This lab demonstrates Create, Read, Update, and Delete operations on Django model objects using the ORM.

## Structure
- `manage.py`: Django management script
- `settings.py`: Django settings
- `crud/`: Contains model definitions and CRUD logic
- `read_courses.py`, `read_instructors.py`, `read_learners.py`, `write.py`: Scripts for CRUD operations

## Setup
1. Create a virtual environment: `python -m venv djangoenv`
2. Activate and install dependencies: `pip install django`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Run scripts to test CRUD operations.

## Notes
- Uses SQLite3 by default.
- See scripts for usage examples.

## Detailed Explanation of CRUD Implementation

This lab provides hands-on examples of how to perform CRUD (Create, Read, Update, Delete) operations using Django's ORM. The implementation is organized into scripts that demonstrate each operation on models such as Course, Instructor, Learner, Enrollment, and Lesson.

### Create
Objects are created using the Django ORM's `Model.objects.create()` method or by instantiating a model and calling `save()`. For example, in `write.py`, new courses, instructors, learners, enrollments, and lessons are created and saved to the database.

### Read
Reading data is performed using query methods like `Model.objects.all()`, `Model.objects.filter()`, and `Model.objects.get()`. Scripts such as `read_courses.py`, `read_instructors.py`, and `read_learners.py` show how to retrieve and display objects based on various criteria, including filtering by field values and using complex queries.

### Update
To update an object, retrieve it from the database, modify its fields, and call `save()`. The scripts demonstrate updating fields such as names or other attributes after fetching objects with queries.

### Delete
Deleting objects is done using the `delete()` method on model instances or querysets. For example, you can remove a learner or instructor by calling `obj.delete()` after retrieving the object.

### Example Workflow
1. `write.py` cleans the database and creates new objects for all models.
2. `read_courses.py`, `read_instructors.py`, and `read_learners.py` demonstrate how to read and filter objects.
3. You can modify objects in the scripts to test update and delete operations.

### Benefits
- Demonstrates the power and flexibility of Django ORM for database management.
- Shows how to structure scripts for automated data handling and testing.
- Provides a foundation for building more complex Django applications with robust data operations.