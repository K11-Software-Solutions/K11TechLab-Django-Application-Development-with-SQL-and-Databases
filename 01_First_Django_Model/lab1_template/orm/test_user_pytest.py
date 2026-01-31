import pytest
from orm.models import User
from datetime import date

@pytest.mark.django_db
def test_create_user_with_required_fields():
    user = User.objects.create(
        first_name="Alice",
        last_name="Smith"
    )
    assert user.first_name == "Alice"
    assert user.last_name == "Smith"

@pytest.mark.django_db
def test_create_user_with_all_fields():
    user = User.objects.create(
        first_name="Bob",
        last_name="Jones",
        dob=date(1990, 5, 20),
        email="bob@example.com",
        phone="1234567890",
        address="123 Main St"
    )
    assert user.email == "bob@example.com"
    assert user.phone == "1234567890"
    assert user.address == "123 Main St"
    assert user.dob == date(1990, 5, 20)

@pytest.mark.django_db
def test_email_uniqueness():
    User.objects.create(first_name="Tom", last_name="Lee", email="unique@example.com")
    with pytest.raises(Exception):
        User.objects.create(first_name="Tim", last_name="Ray", email="unique@example.com")
