FROM python:3

COPY requirements.txt /analysis/requirements.txt
WORKDIR /analysis

RUN pip install -r requirements.txt

COPY . /analysis
CMD [ "python", "./app.py" ]
