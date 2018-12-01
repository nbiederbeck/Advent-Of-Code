days=$(addsuffix .py, \
	 01/01 \
)

.PHONY: all
all: $(days)
	@printf "Advent of Code 2018\n===================\n"
	@for day in $^; do python $$day; done

.PHONY: test
test: $(days)
	pytest $^
