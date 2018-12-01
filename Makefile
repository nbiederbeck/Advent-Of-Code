years=2018
all: $(years)
	make -C $^

test: $(years)
	make -C $^ test

.PHONY: all test
