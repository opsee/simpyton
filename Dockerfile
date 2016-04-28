FROM python:2.7
MAINTAINER <dan@opsee.co>
ARG SIMPYTON_VERSION
ARG SIMPYTON_HOST
ARG SIMPYTON_PORT
ENV SIMPYTON_VERSION ${SIMPYTON_VERSION:-""}
ENV SIMPYTON_HOST ""
ENV SIMPYTON_PORT "8000"

RUN mkdir /home/simpyton
WORKDIR /home/simpyton

COPY . /home/simpyton
RUN pip install -r requirements.txt && pip install .
