# Django specific settings
import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# Your application specific imports
from standalone.models import Test

# Delete all data

# Test Django Model Setup

import pytest
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from standalone.models import Test

@pytest.mark.django_db
def test_create_test_model():
    obj = Test.objects.create(name="Sample")
    assert obj.name == "Sample"
    assert Test.objects.count() == 1

@pytest.mark.django_db
def test_update_test_model():
    obj = Test.objects.create(name="Initial")
    obj.name = "Updated"
    obj.save()
    updated = Test.objects.get(id=obj.id)
    assert updated.name == "Updated"

@pytest.mark.django_db
def test_delete_test_model():
    obj = Test.objects.create(name="ToDelete")
    obj_id = obj.id
    obj.delete()
    assert not Test.objects.filter(id=obj_id).exists()