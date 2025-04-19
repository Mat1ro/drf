# materials/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from materials.models import Course, Lesson
from users.models import Subscription, User


class LessonCourseTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        User.objects.all().delete()

        self.user = User.objects.create(
            email='user@example.com',
            password='password123',
        )
        self.other_user = User.objects.create(
            email='other@example.com',
            password='password456',
        )

        self.course = Course.objects.create(title='Курс 1', description='Описание курса')

        self.lesson = Lesson.objects.create(
            course=self.course,
            title='Урок 1',
            description='Описание урока',
            video_url='https://youtube.com/test'
        )
