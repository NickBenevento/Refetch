.PHONY: all clean test

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

run:
	uvicorn api.main:app --reload

logs:
	docker compose logs -f

clean:
	rm -rf __pycache__ *.pyc

test:
	PYTHONPATH=. pytest api/tests