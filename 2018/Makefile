days=$(addsuffix .py, \
	 dec01/dec01 \
	 dec02/dec02 \
	 dec03/dec03 \
)

all: $(days)
	@printf "Advent of Code 2018\n===================\n"
	@for day in $^; do python $$day; done

test: $(days)
	@pytest $^

.PHONY: all test
