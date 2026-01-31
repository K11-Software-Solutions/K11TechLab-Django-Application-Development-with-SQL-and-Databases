
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from .models import Course, Instructor, Learner, Lesson, Enrollment
from django.urls import reverse
from django.utils import timezone

class CourseModelTest(TestCase):
	def setUp(self):
		User = get_user_model()
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.instructor = Instructor.objects.create(user=self.user, full_time=True, total_learners=0)
		self.course = Course.objects.create(
			name='Test Course',
			image='course_images/test.jpg',
			description='A test course',
			pub_date=timezone.now().date(),
			total_enrollment=5
		)
		self.course.instructors.add(self.instructor)

	def test_course_str(self):
		self.assertIn('Test Course', str(self.course))

	def test_instructor_str(self):
		self.assertEqual(str(self.instructor), 'testuser')

class CourseViewsTest(TestCase):
	def setUp(self):
		User = get_user_model()
		self.user = User.objects.create_user(username='testuser', password='testpass')
		self.instructor = Instructor.objects.create(user=self.user, full_time=True, total_learners=0)
		self.course = Course.objects.create(
			name='Test Course',
			image='course_images/test.jpg',
			description='A test course',
			pub_date=timezone.now().date(),
			total_enrollment=5
		)
		self.course.instructors.add(self.instructor)
		self.client = Client()

	def test_popular_course_list_view(self):
		url = reverse('onlinecourse:popular_course_list')
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test Course')

	def test_course_details_view(self):
		url = reverse('onlinecourse:course_details', args=[self.course.id])
		response = self.client.get(url)
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'Test Course')
