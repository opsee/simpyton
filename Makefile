.PHONY: all build
SIMPYTON_VERSION ?= $(shell git rev-parse HEAD)
SIMPYTON_HOST_PORT ?= 8000
SIMPYTON_PORT ?= 8000

all: build

clean:
	docker rm -vf quay.io/opsee/simpyton

build:
	docker build --build-arg SIMPYTON_VERSION=${SIMPYTON_VERSION} -t quay.io/opsee/simpyton:${SIMPYTON_VERSION} .

run:
	docker run -p ${SIMPYTON_HOST_PORT}:${SIMPYTON_PORT} quay.io/opsee/simpyton:${SIMPYTON_VERSION}
