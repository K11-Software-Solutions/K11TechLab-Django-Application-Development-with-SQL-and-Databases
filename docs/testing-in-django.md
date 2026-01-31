# Automated Testing in Django: Built-in and Pytest

Testing is essential for reliable Django applications. Here’s how to use Django’s built-in test framework and pytest for automated testing.

## 1. Django Built-in Test Framework
- Uses Python’s standard `unittest` module.
- Test cases are written as classes in `tests.py` or a `tests/` folder in your app.
- Run all tests with:
  ```sh
  python manage.py test
  ```
- Example test:
  ```python
  from django.test import TestCase
  from .models import User

  class UserModelTest(TestCase):
      def test_create_user(self):
          user = User.objects.create(first_name="Alice", last_name="Smith")
          self.assertEqual(user.first_name, "Alice")
  ```

## 2. Pytest and pytest-django
- Pytest is a popular, feature-rich testing tool.
- `pytest-django` plugin integrates pytest with Django.
- Install with:
  ```sh
  pip install pytest pytest-django
  ```
- Create a `pytest.ini` file in your project root:
  ```ini
  [pytest]
  DJANGO_SETTINGS_MODULE = myproject.settings
  python_files = tests.py test_*.py *_tests.py
  ```
- Run tests with:
  ```sh
  pytest
  ```
- Pytest allows for simpler test functions and powerful fixtures.
- Example test:
  ```python
  import pytest
  from .models import User

  @pytest.mark.django_db
  def test_create_user():
      user = User.objects.create(first_name="Bob", last_name="Jones")
      assert user.first_name == "Bob"
  ```

## Resources
- [Django Testing Docs](https://docs.djangoproject.com/en/stable/topics/testing/)
- [pytest-django Docs](https://pytest-django.readthedocs.io/)

---
Both methods are widely used. Start with Django’s built-in test runner, and use pytest for more advanced testing needs.
