SHELL := /bin/bash
TAG=adventofcode

build:
	docker build -f Dockerfile \
	-t $(TAG) .

run:
	docker run -it --init -d --runtime=nvidia \
		-v $(PWD):/app/ \
		--gpus=all \
		--ipc=host \
		--publish="2233:2233" \
		--publish="2234:2234" \
		$(TAG) /bin/bash

ruff:
	ruff format . 	