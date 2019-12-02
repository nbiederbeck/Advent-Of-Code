all: test
	python adventofcode.py

test:
	pytest

.PHONY: all test
