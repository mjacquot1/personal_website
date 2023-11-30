from django.core.mail import send_mail

from celery import shared_task

# Async send email
@shared_task(name='tasks.a_send_basic_email')
def a_send_basic_email(email_subject='', email_message='', from_email='mjacquot.dev@gmail.com', to_emails=[], fail_silent=True):
    send_mail(
        email_subject,
        email_message,
        from_email,
        to_emails,
        fail_silently=fail_silent,
    )