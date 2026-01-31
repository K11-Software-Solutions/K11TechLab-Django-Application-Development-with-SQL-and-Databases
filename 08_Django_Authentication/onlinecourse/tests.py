

from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTestCase(TestCase):
	def setUp(self):
		self.username = 'testuser'
		self.password = 'testpass123'
		self.user = User.objects.create_user(username=self.username, password=self.password)
		self.client = Client()

	def test_login(self):
		login = self.client.login(username=self.username, password=self.password)
		self.assertTrue(login)

	def test_logout(self):
		self.client.login(username=self.username, password=self.password)
		self.client.logout()
		response = self.client.get(reverse('onlinecourse:popular_course_list'))
		self.assertEqual(response.status_code, 200)

	def test_registration(self):
		url = reverse('onlinecourse:register')
		response = self.client.post(url, {
			'username': 'newuser',
			'password1': 'newpass123',
			'password2': 'newpass123',
		})
		# Registration should redirect or show success
		self.assertIn(response.status_code, [200, 302])
		# User should exist now
		self.assertTrue(User.objects.filter(username='newuser').exists())

	def test_protected_view_requires_login(self):
		# Try to access a protected view (enroll) without login
		response = self.client.post(reverse('onlinecourse:enroll', args=[1]))
		# Should redirect to login or return 403/302
		self.assertIn(response.status_code, [302, 403])

	def test_protected_view_with_login(self):
		self.client.login(username=self.username, password=self.password)
		# Should be able to access enroll (even if course 1 doesn't exist, should not get 403)
		response = self.client.post(reverse('onlinecourse:enroll', args=[1]))
		# Should not be forbidden
		self.assertNotEqual(response.status_code, 403)
