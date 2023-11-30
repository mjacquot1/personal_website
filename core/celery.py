import os
from celery import Celery
from celery import shared_task
from django.conf import settings
from settings import return_config_env_variables

from django.core.mail import send_mail

config = return_config_env_variables()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', config("DJANGO_SETTINGS_MODULE_ENV"))
app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

@app.task
def divide(x, y):
    import time
    time.sleep(3)
    return x / y

# # Async send email
# @shared_task(bind=True, name='celery.a_send_basic_email')
# def a_send_basic_email(email_subject='', email_message='', from_email='mjacquot.dev@gmail.com', to_emails=[], fail_silent=True):
#     send_mail(
#         email_subject,
#         email_message,
#         from_email,
#         to_emails,
#         fail_silently=fail_silent,
#     )