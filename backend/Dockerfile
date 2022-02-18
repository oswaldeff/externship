FROM python:3.9.6

WORKDIR /var/www/

RUN git clone https://github.com/oswaldeff/externship

WORKDIR /var/www/externship/backend/ecommerce

RUN pipenv --python 3.9

RUN pipenv shell

RUN pipenv install -r requirements/prod.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]