FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
RUN news/python manage.py collectstatic
RUN news/python manage.py makemigrations && news/python manage.py migrate
CMD gunicorn --bind 0.0.0.0:$PORT config.wsgi