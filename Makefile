PYTHON_VERSION = 3.10.0
PYTHON_CURRENT_VERSION = $(shell python --version | cut -d " " -f2)

default: run

ifeq ($(shell which poetry), )
	$(info Please run `make install-deps`)
	$(error )
else
	POETRY_PYTHON_VERSION = $(shell poetry env info | grep Python: | sed -e "s/ //g" | cut -d ":" -f2 | head -n 1)
endif

ifneq ($(PYTHON_CURRENT_VERSION), $(PYTHON_VERSION))
	$(info Require python version $(PYTHON_VERSION))
	$(error )
endif

ifneq ($(POETRY_PYTHON_VERSION), $(PYTHON_VERSION))
	@poetry env use $(PYTHON_VERSION)
endif

init: install-deps

install-deps:
	@pip install --upgrade pip setuptools wheel
	@pip install --upgrade poetry

run:
	@poetry install
	@poetry run env $(shell cat .env | grep -v ^\# | xargs) uvicorn src.main:app --reload --port 8080

env:
	@cp .env.template .env

test-all:
	@poetry run env $(shell cat .env | grep -v ^\# | xargs) pytest

poetry-export:
	@poetry export --without-hashes --no-ansi --no-interaction --format requirements.txt --output requirements.txt

build-image: poetry-export
	@docker build -t chargeback-api:latest .

run-docker: build-image
	@docker run --rm -p '8080:8080' --name 'chargeback-api' chargeback-api:latest

add-deps:
ifeq ($(libs), )
	$(info Please run `make add-deps libs="lib1==version ...lib[n]==version"`)
	$(error )
endif
	@poetry add -vv --no-ansi --no-interaction $(libs)

add-dev-deps:
ifeq ($(libs), )
	$(info Please run `make add-dev-deps libs="lib1==version ...lib[n]==version"`)
	$(error )
endif
	@poetry add -vv --no-ansi --no-interaction --dev $(libs)

rm-deps:
ifeq ($(libs), )
	$(info Please run `make rm-deps libs="lib1 ...lib[n]"`)
	$(error )
endif
	@poetry remove -vv --no-ansi --no-interaction $(libs)

rm-dev-deps:
ifeq ($(libs), )
	$(info Please run `make rm-dev-deps libs="lib1 ...lib[n]"`)
	$(error )
endif
	@poetry remove -vv --no-ansi --no-interaction --dev $(libs)

setup-db-test:
	@docker run -d --rm \
		--name finops \
		-e POSTGRES_PASSWORD=postgres \
		-e POSTGRES_USER=postgres \
		-e POSTGRES_DB=postgres \
		-p 5432:5432 postgres:13-alpine
