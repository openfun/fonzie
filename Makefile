#
# GLOBALS
#
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

# Dockerized tools
# -- Docker
COMPOSE            = bin/compose
COMPOSE_BUILD      = bin/build
COMPOSE_RUN        = bin/run
COMPOSE_RUN_LMS    = $(COMPOSE_RUN) lms
COMPOSE_RUN_FONZIE = $(COMPOSE_RUN) fonzie
COMPOSE_RUN_NODE   = $(COMPOSE_RUN) node

# -- Python
COVERAGE    = $(COMPOSE_RUN_LMS) coverage
DIFF-COVER  = $(COMPOSE_RUN_FONZIE) diff-cover
PYTEST      = bin/pytest

# -- Node
YARN = $(COMPOSE_RUN_NODE) yarn

#
# RULES
#
default: help

help: ## display this help message
	@echo "Please use \`make <target>' where <target> is one of"
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-25s\033[0m %s\n", $$1, $$2}'
.PHONY: help

bootstrap: build ## bootstrap the project
	$(COMPOSE_RUN_LMS) python manage.py lms migrate
.PHONY: bootstrap

build: ## build project containers
	$(COMPOSE_BUILD) lms
	$(COMPOSE_RUN) --no-deps node yarn install
.PHONY: build

clean: ## remove generated byte code, coverage reports, and build artifacts
	$(COMPOSE_RUN_FONZIE) find . -name '__pycache__' -exec rm -rf {} +
	$(COMPOSE_RUN_FONZIE) find . -name '*.pyc' -exec rm -f {} +
	$(COMPOSE_RUN_FONZIE) find . -name '*.pyo' -exec rm -f {} +
	$(COMPOSE_RUN_FONZIE) find . -name '*~' -exec rm -f {} +
	$(COMPOSE_RUN) --no-deps lms coverage erase
	$(COMPOSE_RUN_FONZIE) rm -fr build/
	$(COMPOSE_RUN_FONZIE) rm -fr dist/
	$(COMPOSE_RUN_FONZIE) rm -fr *.egg-info
.PHONY: clean

coverage: clean ## generate and view HTML coverage report
	$(PYTEST) --cov-report html
	$(BROWSER) htmlcov/index.html
.PHONY: coverage

diff_cover: test
	$(DIFF-COVER) edx-platform/reports/coverage.xml
.PHONY: diff_cover

docs: ## generate Sphinx HTML documentation, including API docs
	$(COMPOSE_RUN_FONZIE) doc8 --ignore-path docs/_build README.rst docs
	rm -f docs/fonzie.rst
	rm -f docs/modules.rst
	$(COMPOSE_RUN_FONZIE) make -C docs clean
	$(COMPOSE_RUN_FONZIE) make -C docs html
	$(COMPOSE_RUN_FONZIE) python setup.py check --restructuredtext --strict
	$(BROWSER) docs/_build/html/index.html
.PHONY: docs

quality: ## check coding style with pycodestyle and pylint
	touch tests/__init__.py
	$(COMPOSE_RUN_FONZIE) pylint fonzie tests test_utils
	$(COMPOSE_RUN_FONZIE) pylint --py3k fonzie tests test_utils
	rm tests/__init__.py
	$(COMPOSE_RUN_FONZIE) pycodestyle fonzie tests
	$(COMPOSE_RUN_FONZIE) pydocstyle fonzie tests
	$(COMPOSE_RUN_FONZIE) isort --check-only --recursive tests test_utils fonzie manage.py setup.py
	${MAKE} selfcheck
	$(COMPOSE_RUN_FONZIE) pyroma .
.PHONY: quality

run: ## start development server
	$(COMPOSE) up -d lms
.PHONY: run

selfcheck: ## check that the Makefile is well-formed
	@echo "The Makefile is well-formed."
.PHONY: selfcheck

stop:  ## stop development server
	$(COMPOSE) stop
.PHONY: stop

test: clean ## run python tests suite
	$(PYTEST)
.PHONY: test

test-spec: ## run tests on API specification (API blueprint)
	$(COMPOSE) up -d lms
	$(COMPOSE_RUN_LMS) dockerize -wait tcp://mysql:3306 -timeout 60s
	$(YARN) dredd
.PHONY: test-spec

validate: quality test ## run tests and quality checks
.PHONY: validate
