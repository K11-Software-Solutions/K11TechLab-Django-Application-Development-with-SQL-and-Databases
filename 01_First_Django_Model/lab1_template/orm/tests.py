from django.test import TestCase
from orm.models import User
from datetime import date

class UserModelTest(TestCase):
    def test_create_user_with_required_fields(self):
        user = User.objects.create(
            first_name="Alice",
            last_name="Smith"
        )
        self.assertEqual(user.first_name, "Alice")
        self.assertEqual(user.last_name, "Smith")

    def test_create_user_with_all_fields(self):
        user = User.objects.create(
            first_name="Bob",
            last_name="Jones",
            dob=date(1990, 5, 20),
            email="bob@example.com",
            phone="1234567890",
            address="123 Main St"
        )
        self.assertEqual(user.email, "bob@example.com")
        self.assertEqual(user.phone, "1234567890")
        self.assertEqual(user.address, "123 Main St")
        self.assertEqual(user.dob, date(1990, 5, 20))

    def test_email_uniqueness(self):
        User.objects.create(first_name="Tom", last_name="Lee", email="unique@example.com")
        with self.assertRaises(Exception):
            User.objects.create(first_name="Tim", last_name="Ray", email="unique@example.com")
