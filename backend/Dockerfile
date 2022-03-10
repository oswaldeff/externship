FROM python:3.9.6

WORKDIR /var/www/

RUN git clone https://github.com/oswaldeff/externship.git

WORKDIR /var/www/externship/backend

RUN python -m pip install --upgrade pip

RUN pip3 install -r ecommerce/requirements/prod.txt

RUN pip3 install gunicorn

WORKDIR /var/www/externship/backend/ecommerce

EXPOSE 8000

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]