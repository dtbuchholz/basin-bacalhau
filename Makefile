install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

build:
	docker buildx build --platform linux/amd64 -t dtbuchholz/wxm . --load

publish:
	docker push dtbuchholz/wxm

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