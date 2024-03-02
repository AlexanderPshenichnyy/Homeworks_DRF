from rest_framework.test import APITestCase, force_authenticate, APIClient
from rest_framework import status
from rest_framework.response import Response
from users.models import User
from lms.models import Lesson, Course, Subscription
from django.urls import reverse
from lms.views import LessonListAPIView


class CRUDTestCase(APITestCase):
    def setUp(self):
        self.url = ''
        self.data = {}
        self.user = User.objects.create(
            username="Test",
            password="1234"
        )
        self.course = Course.objects.create(
            title="Django"
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_all_lessons(self):
        response = self.client.get(reverse("lms:all_lessons"))
        if self.assertEqual(response.status_code, status.HTTP_200_OK):
            print('200')

    def test_create_lesson(self):
        self.url = "lms:create_lesson"
        self.data = {
            "title": "lesson",
            "description": "1",
            "link": "https://www.youtube.com/watch?13214432",
            "course_id": 1
        }
        response = self.client.post(reverse(self.url), self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_add(self):
        data = {'course': self.course.id}
        response = self.client.post(reverse('lms:subscribe'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['message'], 'Подписка добавлена')
        self.assertEqual(Subscription.objects.count(), 1)
