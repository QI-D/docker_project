FROM python:3

COPY requirements.txt /backend/requirements.txt
WORKDIR /backend

RUN pip install -r requirements.txt

COPY . /backend
CMD [ "python", "./app.py" ]
