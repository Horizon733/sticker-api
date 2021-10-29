FROM python:3.7.5-stretch AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

ADD requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt

ADD main.py main.py
ADD query.py query.py