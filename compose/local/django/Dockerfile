FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /requirements.txt

COPY ./compose/local/django/entrypoint /entrypoint
# sed is a stream editor to modify the /entrypoint file with the command:
# '-i' change the file
# 's' for substitute / 
# '\r$' Regular Expression, any carriage return at the end of a string with /
# '' nothing /
# and 'g' is the command to substitute all instances
RUN sed -i 's/\r$//g' /entrypoint
# Authorize the /entrypoint file
RUN chmod +x /entrypoint

# COPY ./compose/local/django/start /start
# RUN sed -i 's/\r$//g' /start
# RUN chmod +x /start

COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower

WORKDIR /app
COPY . .

ENTRYPOINT ["/entrypoint"]

# running migrations
# RUN python manage.py migrate

# gunicorn
# CMD ["gunicorn", "-c", "gunicorn-cfg.py", "core.wsgi"] 
