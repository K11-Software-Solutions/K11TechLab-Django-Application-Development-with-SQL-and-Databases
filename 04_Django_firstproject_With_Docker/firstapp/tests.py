
from django.test import TestCase
from .models import *  # Import your models here

class SampleModelTest(TestCase):
	def test_sample(self):
		# Example: test that 1+1=2
		self.assertEqual(1 + 1, 2)
