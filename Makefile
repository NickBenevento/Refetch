.PHONY: all clean test

all: test

run:
	uvicorn api.main:app --reload

connect_db:
	psql -h 'refetch.cr04sckw0441.us-east-1.rds.amazonaws.com' -U postgres

clean:
	rm -rf __pycache__ *.pyc

test:
	PYTHONPATH=. pytest api/tests