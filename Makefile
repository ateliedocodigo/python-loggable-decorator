
PIP = pip3
PYTHON = python3
PIPY_REPOSITORY=pypi

ifdef PY_VENV_PATH
PYTHON_ACTIVATE = . $(PY_VENV_PATH)/bin/activate
PIP = $(PYTHON_ACTIVATE) && pip
PYTHON_BIN := $(PYTHON)
PYTHON := $(PYTHON_ACTIVATE) && $(PYTHON)
ifneq ("$(wildcard $(PATH_TO_FILE))","")
$(PYTHON_ACTIVATE):
else
$(PYTHON_ACTIVATE):
	virtualenv -p$(PYTHON_BIN) $(PY_VENV_PATH)
endif
endif

.PHONY: clean
clean:
	rm -rf dist/

.PHONY: install
install:
	$(PYTHON) setup.py install

# make test PY_VENV_PATH=env
.PHONY: test
test: install
	$(PYTHON) examples/example-1.py
	$(PYTHON) examples/example-2.py

.PHONY: register
register:
	$(PYTHON) setup.py register -r ${PIPY_REPOSITORY}

.PHONY: dist
dist:
	$(PYTHON) setup.py sdist

.PHONY: upload
upload:
	$(PYTHON) setup.py sdist upload -r ${PIPY_REPOSITORY}

ifndef VERBOSE
.SILENT:
endif
