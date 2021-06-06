FROM ubuntu:18.04


RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip

COPY . /app

WORKDIR /app/

RUN python3 --version
RUN pip3 --version
RUN pip3 install -r requirements.txt
RUN pip3 freeze

EXPOSE 8000

CMD python3 manage.py runserver
