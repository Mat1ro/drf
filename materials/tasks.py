from celery import shared_task
from django.core.mail import send_mail

from drf import settings
from materials.models import Course
from users.models import Subscription


@shared_task
def course_update(course_id) -> None:
    course = Course.objects.get(id=course_id)
    subscribes = Subscription.objects.filter(course=course)
    recipients = []
    for sub in subscribes:
        recipients.append(sub.user.email)
    if recipients:
        send_mail(
            subject=f"Курс '{course.title}' обновился",
            message=f"Курс '{course.title}' был обновлен. Проверьте новые материалы!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipients,
        )
