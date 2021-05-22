FROM ubuntu
MAINTAINER Gayathri
RUN apt-get update -y
RUN apt-get install -y python
RUN apt-get install -y python3-pip
RUN python3 -m pip install tweepy
RUN mkdir -p /src/app
WORKDIR /src/app
COPY . /src/app
CMD [ "python3", "./twitter_api1.py" ]