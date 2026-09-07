install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl --force

publish:
	uv publish --dry-run

lint:
	uv run ruff check --config=./ruff.toml gendiff

test:
	uv run pytest -vv --color=yes tests

test-coverage:
	uv run pytest --cov=gendiff --cov-report term --cov-report xml tests

check: lint test
