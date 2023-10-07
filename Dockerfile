FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY ./entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint


WORKDIR /app
COPY . .

ENTRYPOINT ["/entrypoint"]

# running migrations
# RUN python manage.py migrate

# gunicorn
# CMD ["gunicorn", "-c", "gunicorn-cfg.py", "core.wsgi"] 
