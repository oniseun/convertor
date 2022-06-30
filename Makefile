test:
	poetry run python -m pytest

mypy:
	bin/run-mypy.sh

lint:  mypy _formatters

_formatters:
	bin/run-black.sh && \
	bin/run-flake8.sh

run:
	poetry run python -m boilerplate

bump-version:
	bin/bump-version.sh