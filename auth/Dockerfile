FROM python:3

COPY requirements.txt /auth/requirements.txt
WORKDIR /auth

RUN pip install -r requirements.txt

COPY . /auth

CMD [ "python", "./app.py" ]