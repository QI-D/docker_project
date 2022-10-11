FROM python:3

COPY requirements.txt /storage/requirements.txt
WORKDIR /storage

RUN pip install -r requirements.txt

COPY . /storage
CMD [ "python", "./app.py" ]
