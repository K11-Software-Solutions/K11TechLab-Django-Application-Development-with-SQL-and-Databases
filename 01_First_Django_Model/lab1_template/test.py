# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Your application specific imports
from orm.models import User
from datetime import date

# Delete all data
def clean_data():
    User.objects.all().delete()

# Test Django Model Setup
def test_setup():
    try:
        clean_data()
        # Create a test user with all fields and save to database
        user = User(
            first_name='John',
            last_name='Doe',
            dob=date(1970, 3, 16),
            email='john.doe@example.com',
            phone='555-1234',
            address='123 Main St'
        )
        user.save()
        # Check user table is not empty
        assert User.objects.count() == 1
        db_user = User.objects.first()
        assert db_user.first_name == 'John'
        assert db_user.last_name == 'Doe'
        assert db_user.dob == date(1970, 3, 16)
        assert db_user.email == 'john.doe@example.com'
        assert db_user.phone == '555-1234'
        assert db_user.address == '123 Main St'
        print("Django Model setup completed and all fields verified.")
    except AssertionError as exception:
        print("Django Model setup failed with error: ")
        raise(exception)
    except Exception as e:
        print(f"Unexpected error: {e}")

test_setup()