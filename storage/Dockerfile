FROM qidang/project1:storage

RUN apt install python3-pip -y

COPY requirements.txt /storage/requirements.txt

WORKDIR /storage
RUN pip3 install -r requirements.txt
RUN service mysql start

COPY . /storage

EXPOSE 8090
CMD ["python3", "./app.py"]
