FROM ubuntu
RUN apt update
RUN apt install npm -y

WORKDIR /frontend

RUN npm install http-server -g

COPY . /frontend

EXPOSE 8091
CMD ["http-server", "-p", "8091"]
