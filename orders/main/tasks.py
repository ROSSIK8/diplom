from .models import EmailConfirmation
from django.conf import settings
from django.core.mail import send_mail

from orders.celery_app import app


@app.task()
def send_email_code(user_id, email, code):
    send_mail('Код подтверждения', f'{code}', settings.EMAIL_HOST_USER, [email])
    EmailConfirmation.objects.create(user_id=user_id, email=email, code=code)

