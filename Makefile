build:
	docker-compose build --no-cache

up:
	docker-compose up

down:
	docker-compose down

rebuild: down build up

force-recreate:
	docker-compose up --force-recreate --build

.PHONY: build up down rebuild force-recreate
