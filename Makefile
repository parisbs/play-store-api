include .env
export $(shell sed 's/=.*//' .env)

run:
	gunicorn --reload -b :$(API_PORT) play_store_api.api:api

install: install-deps install-githooks

install-server:
	pip install -r requirements.txt

install-deps:
	pip install --upgrade pip
	pip install -r requirements.txt

install-githooks:
	cp git-hooks/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit

test-all:
	tox

test:
	tox -e py368

unit-tests:
	tox -e py368 tests/unit

functional-tests:
	tox -e py368 tests/functional

lint:
	tox -e linters

coverage:
	tox -e coverage

clean:
	rm -rf .tox

.PHONY: run install install-server install-deps install-githooks test-all test unit-tests functional-tests lint coverage clean
