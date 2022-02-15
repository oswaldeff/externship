FROM python:3.9.6

WORKDIR /var/www/

RUN git clone https://github.com/oswaldeff/backend-mission

WORKDIR /var/www/backend-misiion/missions/week 5/back/

RUN pipenv install -r ABLY-externship-5/requirements/prod.txt

RUN python manage.py migrate

EXPOSE 8000

CMD