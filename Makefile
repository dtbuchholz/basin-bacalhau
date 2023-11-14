install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

buildx-create:
	docker buildx create --name basin-builder --use

buildx-inspect:
	docker buildx inspect --bootstrap

build:
	docker buildx build --platform linux/amd64 -t dtbuchholz/basin . --load

publish:
	docker push dtbuchholz/basin

up-build:
	docker compose build --no-cache

up:
	docker-compose up

down:
	docker-compose down

local:
	python main.py

job-local:
	python job.py