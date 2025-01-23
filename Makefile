SHELL := /bin/bash
ENV=dev
folder_name =$(shell basename $(shell pwd))
function_name = $(subst _,-,$(folder_name))

.PHONY: init requirements requirements-all test lint package deploy clean clean-all

init:
	rm -rf .venv
	python3 -m venv .venv && \
	source .venv/bin/activate 

requirements:
	source .venv/bin/activate && \
	pip install -r requirements.txt 

requirements-all: requirements
	source .venv/bin/activate && \
	[ -f ./tests/requirements.txt ] && pip install -r ./tests/requirements.txt && \
	[ -f ./requirements.dev.txt ] && pip install -r ./requirements.dev.txt

test:
	source .venv/bin/activate && \
	coverage run --omit '.venv/*' -m pytest -o junit_suite_name=$(folder_name) --junitxml=./test-results/test-results.xml  -v tests/ && \
	coverage report -m

lint:
	source .venv/bin/activate && \
	pip install pylint && \
	pylint --fail-under=8 ./src ./lambda_function.py

clean:
	rm -rf pkg/ && \
	rm -f .coverage

package: clean
	mkdir ./pkg && \
	cd .venv/lib/python*/ && \
	cp -r site-packages/ deploy-packages/ && \
	cd deploy-packages && \
	rm -rf boto* pip* && \
	zip -r ../../../../pkg/deployment-package.zip . && \
	cd ../../../../ && \
	zip -gr pkg/deployment-package.zip src/ ./lambda_function.py

# deploy:
# 	aws lambda --profile $(ENV)-pinpoint update-function-code --function-name ${ENV}-$(function_name) --zip-file fileb://pkg/deployment-package.zip --publish


# clean-all:
# 	rm -rf .venv/ && \
# 	rm -rf pkg/ && \
# 	rm -f .coverage
