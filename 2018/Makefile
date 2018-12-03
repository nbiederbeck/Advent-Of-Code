days=$(addsuffix /solution.py, \
	 dec01 \
)

all: $(days)
	@printf "Advent of Code 2018\n===================\n"
	@for day in $^; do python $$day; done

test: $(days)
	@pytest $^

.PHONY: all test
