FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .

# running migrations
# RUN python manage.py migrate

# gunicorn
# This calls gunicorn to run core.wsgi with the gunicorn-cfg.py configuration file by using the -c (--config) command
CMD ["gunicorn", "-c", "gunicorn-cfg.py", "core.wsgi"] 
