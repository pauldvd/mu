# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# Install python3
RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-venv

# Create venv
ENV VIRTUAL_ENV_DIR=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV_DIR
ENV VIRTUAL_ENV=$VIRTUAL_ENV_DIR

# Install dependencies and copy src code
WORKDIR /src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src .

