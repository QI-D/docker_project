FROM ubuntu

RUN apt update
RUN apt install -y python3 python3-pip

COPY requirements.txt /backend/requirements.txt

WORKDIR /backend

RUN pip3 install -r requirements.txt
COPY . /backend

EXPOSE 8080
CMD ["python3", "./app.py"]
