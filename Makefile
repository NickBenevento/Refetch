.PHONY: all clean test

POSTGRES_CONTAINER_NAME=local-postgres
DB_NAME=postgres

all: test

up:
	docker compose up -d

psql:	# log in to the postgres container
	docker exec -it local-postgres psql -U ${DB_NAME}
# exec --> run command inside container
# i --> interactive (i.e. can type)

down:
	docker compose down

restart:
	docker compose down && docker compose up -d

clean_db:
	docker exec -it ${POSTGRES_CONTAINER_NAME} psql -U postgres -d ${DB_NAME} -c "DROP SCHEMA public CASCADE; CREATE SCHEMA public;"

run:
	uvicorn api.main:app --reload

logs:
	docker compose logs -f

test:
	PYTHONPATH=. pytest api/tests