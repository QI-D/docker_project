FROM ubuntu
RUN apt update
RUN apt install npm -y

WORKDIR /results

RUN npm install http-server -g

COPY . /results

CMD ["http-server", "-p", "5000"]
