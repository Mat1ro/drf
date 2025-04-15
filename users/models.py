from django.contrib.auth.models import AbstractUser
from django.db import models

from drf.settings import NULLABLE
from materials.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email")
    phone = models.CharField(max_length=20, **NULLABLE)
    city = models.CharField(max_length=100, **NULLABLE)
    avatar = models.ImageField(upload_to='avatars/', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENT_TYPE_CHOICES = [
        ('cash', 'Наличка'),
        ('transfer', 'Перевод'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    payment_date = models.DateField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.email} course: {self.course.title}, lesson: {self.lesson.title}, amount: {self.amount}"
