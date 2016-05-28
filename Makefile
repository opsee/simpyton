.PHONY: all build
SIMPYTON_VERSION ?= $(shell git rev-parse HEAD)

all: build

clean:
	docker rm -vf quay.io/opsee/simpyton

build:
	docker build --build-arg SIMPYTON_VERSION=${SIMPYTON_VERSION} -t quay.io/opsee/simpyton:${SIMPYTON_VERSION} .

run:
	docker run quay.io/opsee/simpyton:${SIMPYTON_VERSION}
