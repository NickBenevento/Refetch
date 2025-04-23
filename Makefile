.PHONY: all clean test

all: test

run:
	fastapi dev api/main.py

clean:
	rm -rf __pycache__ *.pyc

test:
	python -m pytest