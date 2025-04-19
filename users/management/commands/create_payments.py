from django.core.management.base import BaseCommand

from users.models import Payments, User


class Command(BaseCommand):
    help = 'Создание дефолтных записей для проверки'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Payments.objects.all().delete()
        user = User.objects.create(
            email='email@example.com',
            first_name='Name',
            last_name='Surname',
            is_staff=True,
            is_superuser=True,
        )
        user = User.objects.get(email='email@example.com')
        user.set_password('password')
        user.save()
        Payments.objects.create(
            user=user,
            course_id=1,
            lesson_id=1,
            price=1000,
            payment_type="cash",
        )
        Payments.objects.create(
            user=user,
            course_id=1,
            lesson_id=2,
            price=1200,
            payment_type="transfer",
        )
