FROM gliderlabs/alpine:3.3

WORKDIR /myapp
COPY . /myapp

ARG SIMPYTON_VERSION
ENV SIMPYTON_VERSION ${SIMPYTON_VERSION:-""}

RUN apk --update add python py-pip openssl ca-certificates
RUN apk --update add --virtual build-dependencies python-dev build-base wget \
  && pip install -r requirements.txt \
  && python setup.py install \
  && apk del build-dependencies

EXPOSE 8000
CMD ["python", "simpyton"]
