FROM python:3.7-alpine3.8
MAINTAINER Vallard Benincosa <vallard@benincosa.com>

RUN pip install --no-cache python-twitter

ADD twitter-scrape.py . 
