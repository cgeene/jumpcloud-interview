build:
	docker-compose build
push:
	docker-compose push
up:
	docker-compose up --remove-orphans
buildup:
	docker-compose up --build --remove-orphans
initdb:
	docker-compose build
	docker-compose run jumpcloud init-db
down:
	docker-compose down
reset:
	docker-compose down -v --remove-orphans && docker-compose rm -v
