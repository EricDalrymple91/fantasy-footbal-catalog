.PHONY: build uv test

build:
	@.scripts/docker-build.sh

uv:
	@.scripts/uv.sh

test:
	@docker compose run --rm test