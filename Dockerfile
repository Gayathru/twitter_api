FROM python:alpine3.7
MAINTAINER Gayathri
RUN python3 -m pip install tweepy
RUN python3 -m pip install flask
RUN python3 -m pip install python-decouple
RUN mkdir -p /src/app
WORKDIR /src/app
COPY . /src/app
CMD [ "python3", "./app.py"]
